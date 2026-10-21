#!/usr/bin/env bash
set -Eeuo pipefail
systemctl list-units --type=service --state=active,activating \
  'yila-skills-ci-once-*' --no-legend --plain
