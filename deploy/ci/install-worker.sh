#!/usr/bin/env bash
# Install on the CI host. No long-lived GitHub credential is needed here.
set -Eeuo pipefail
[[ $(id -u) == 0 ]] || { echo 'root required' >&2; exit 1; }
source_dir="$(cd -- "$(dirname -- "$0")" && pwd)"
docker image inspect yila-pr-ci:2.337.0 >/dev/null
docker network inspect yila-pr-ci >/dev/null
install -m 0755 "$source_dir/worker.sh" /usr/local/sbin/yila-skills-ci-once
install -m 0755 "$source_dir/start-worker.sh" /usr/local/sbin/yila-skills-ci-start
install -m 0755 "$source_dir/status.sh" /usr/local/sbin/yila-skills-ci-status
echo 'Installed isolated one-job Skills runner helpers.'
