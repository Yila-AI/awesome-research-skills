#!/usr/bin/env bash
# Exactly one job/identity; root-owned helper on the CI host.
set -Eeuo pipefail
nonce="${1:?nonce}"
[[ "$nonce" =~ ^[0-9]+-[0-9]+$ ]] || exit 64
volume="yila-skills-ci-once-$nonce"
worker_name="yila-skills-ci-$nonce"
cleanup() {
  docker stop --time 20 "$worker_name" >/dev/null 2>&1 || true
  docker volume rm "$volume" >/dev/null 2>&1 || true
}
trap cleanup EXIT
trap 'exit 143' TERM
trap 'exit 130' INT
docker run --rm --name "$worker_name" \
  --network yila-pr-ci --user 1001:1001 \
  --cap-drop ALL --security-opt no-new-privileges \
  --memory 4g --memory-swap 4g --cpus 2 --pids-limit 1024 --cpu-shares 128 \
  --tmpfs /tmp:rw,size=2g,uid=1001,gid=1001 \
  -v "$volume:/config:ro" \
  -e RUNNER_ALLOW_RUNASROOT=0 yila-pr-ci:2.337.0 &
worker_pid=$!
wait "$worker_pid"
