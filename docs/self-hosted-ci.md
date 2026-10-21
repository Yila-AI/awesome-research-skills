# Self-hosted CI

Yila-AI disables standard GitHub-hosted runners organization-wide. CI and tag
release jobs require `[self-hosted, linux, x64, yila-skills-ci]`; there is no
hosted fallback. CI still tests Python 3.10, 3.11 and 3.12. The pinned setup-uv
action installs managed Python into a per-job environment on the Debian worker.
GitHub Actions caching is disabled. Tag releases retain their existing behavior.

Each job gets a new ephemeral GitHub runner identity, automatically unregistered
after its single job, and a fresh container as uid 1001. The 4 GiB / 2 CPU
container drops all capabilities, allows no new privileges, and has no host
paths or Docker socket. Its read-only registration volume is dedicated to that
one job and removed on exit. Even the runner identity is not reused by another
job. The preinstalled `yila-pr-ci:2.337.0` image and firewalled `yila-pr-ci`
network deny host/control-plane and private-network access, while public GitHub
and Python downloads remain available.

External fork workflow runs require maintainer approval (`all_external_contributors`).
Review workflow and executable-code changes before approving; the registration
controller refuses to start workers if this setting is relaxed. It never
approves fork runs, creates releases or dispatches workflows itself.

Install `deploy/ci/install-worker.sh` on the CI host. The operator Mac runs
`deploy/ci/controller.mjs` once per minute under its existing local GitHub CLI
identity, with `YILA_SKILLS_CI_SSH_HOST` set to the CI host's SSH alias. It polls
only this repository and starts at most one one-shot host unit. Only a one-hour
repository registration token crosses SSH on stdin; the Mac's OAuth/PAT
credential never goes to the host or a job container. No additional token or
credential is committed or stored in a service environment. Host helpers and
the local controller must be installed from reviewed source; never execute a
pull request's copy as the registration controller.

If the Mac is offline/asleep or authentication/SSH is unavailable, jobs queue.
There is no hosted fallback. The host transient unit supervises each job and
cleans its container/registration volume independently of the Mac. Root helper
names are `yila-skills-ci-start`, `yila-skills-ci-status` and `yila-skills-ci-once`.
The local registration broker is `ai.yila.skills-ci-controller`; it is a
control-plane dependency, while all workflow execution happens on the CI host.
