#!/usr/bin/env bash
# Accept ONLY a short-lived repository registration token on stdin.
set -Eeuo pipefail
set +x
umask 077
[[ $(id -u) == 0 ]] || exit 1
exec 9>/run/yila-skills-ci-register.lock
flock -n 9 || exit 75
[[ -z "$(/usr/local/sbin/yila-skills-ci-status)" ]] || exit 75
docker image inspect yila-pr-ci:2.337.0 >/dev/null
docker network inspect yila-pr-ci >/dev/null
IFS= read -r registration_token
[[ -n "$registration_token" ]]
nonce="$(date -u +%s)-$$"
volume="yila-skills-ci-once-$nonce"
started=0
cleanup() {
  if [[ "$started" == 0 ]]; then docker volume rm "$volume" >/dev/null 2>&1 || true; fi
}
trap cleanup EXIT
docker volume create "$volume" >/dev/null
mountpoint="$(docker volume inspect --format '{{.Mountpoint}}' "$volume")"
[[ "$mountpoint" == /var/lib/docker/volumes/"$volume"/_data && ! -L "$mountpoint" ]]
install -d -o 1001 -g 1001 -m 0700 "$mountpoint"
docker run --rm -i --network yila-pr-ci --user 1001:1001 \
  --cap-drop ALL --security-opt no-new-privileges --memory 1g --cpus 0.5 \
  -v "$volume:/config" --entrypoint /bin/bash yila-pr-ci:2.337.0 -c '
    set -Eeuo pipefail
    cd /home/runner/actions-runner
    IFS= read -r token
    ./config.sh --unattended --ephemeral --disableupdate \
      --url https://github.com/Yila-AI/awesome-research-skills \
      --token "$token" --name "webnx-yila-skills-once-$1" \
      --labels yila-skills-ci --work _work
    unset token
    install -m 0600 .runner .credentials .credentials_rsaparams /config/
  ' -- "$nonce" <<< "$registration_token" >/dev/null
unset registration_token
systemd-run --quiet --collect --unit="yila-skills-ci-once-$nonce" \
  --property=KillMode=process --property=TimeoutStopSec=45 \
  /usr/local/sbin/yila-skills-ci-once "$nonce"
started=1
echo "Started one-job ephemeral Skills runner $nonce"
