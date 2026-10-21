#!/usr/bin/env node
// Run on the operator Mac, outside job containers. Never copy its gh identity
// to the CI host. The LaunchAgent runs this bounded poll once per minute.
import { execFileSync } from "node:child_process";
const repository = "Yila-AI/awesome-research-skills";
const host = process.env.YILA_SKILLS_CI_SSH_HOST;
if (!host || !/^[a-zA-Z0-9_.-]+$/.test(host))
  throw new Error("Set YILA_SKILLS_CI_SSH_HOST to an SSH configuration alias");
const prefix = "webnx-yila-skills-once-";
function api(path, method) {
  try {
    const args = ["api"];
    if (method) args.push("--method", method);
    args.push(`repos/${repository}/${path}`);
    const result = execFileSync("gh", args, {
      encoding: "utf8",
      timeout: 30000,
      maxBuffer: 4 * 1024 * 1024,
      stdio: ["ignore", "pipe", "pipe"],
    });
    return result.trim() ? JSON.parse(result) : null;
  } catch {
    throw new Error(`GitHub API request failed (${path.split("?")[0]})`);
  }
}
function ssh(command, input) {
  try {
    return execFileSync(
      "ssh",
      ["-o", "BatchMode=yes", "-o", "ConnectTimeout=10", host, command],
      {
        input,
        encoding: "utf8",
        timeout: 120000,
        stdio: ["pipe", "pipe", "pipe"],
      },
    );
  } catch {
    throw new Error("CI host operation failed; no credential was logged");
  }
}
try {
  if (
    api("actions/permissions/fork-pr-contributor-approval").approval_policy !==
    "all_external_contributors"
  )
    throw new Error("External-fork approval must remain required");
  const runs = ["queued", "in_progress"].flatMap(
    (status) => api(`actions/runs?status=${status}&per_page=20`).workflow_runs,
  );
  const runIds = [...new Set(runs.map((run) => run.id))];
  let queued = false;
  for (const id of runIds) {
    if (
      api(`actions/runs/${id}/jobs?per_page=100`).jobs.some(
        (job) =>
          job.status === "queued" && job.labels.includes("yila-skills-ci"),
      )
    ) {
      queued = true;
      break;
    }
  }
  if (queued && !ssh("/usr/local/sbin/yila-skills-ci-status").trim()) {
    const runners = api("actions/runners?per_page=100").runners.filter(
      (runner) => runner.name.startsWith(prefix),
    );
    for (const runner of runners) {
      // No unit is running on the host, so these are our own finished/crashed
      // one-shot registrations. Never remove another runner's identity.
      if (runner.busy)
        throw new Error(
          "A finished host unit still has an assigned GitHub job; defer",
        );
      api(`actions/runners/${runner.id}`, "DELETE");
    }
    const registration = api("actions/runners/registration-token", "POST");
    // Only this one-hour registration token crosses SSH, on stdin. It is not
    // a PAT/OAuth credential and cannot administer the repository.
    const result = ssh(
      "/usr/local/sbin/yila-skills-ci-start",
      registration.token + "\n",
    );
    console.log(new Date().toISOString(), result.trim());
  }
} catch (error) {
  console.error(new Date().toISOString(), error.message);
  process.exitCode = 1;
}
