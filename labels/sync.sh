#!/bin/sh
# Create or update the organisation's shared labels in a repository.
#
#   labels/sync.sh OWNER/REPO            add and update the shared labels
#   labels/sync.sh OWNER/REPO --prune    also delete GitHub's default labels that issue types replace
#
# Labels a repository adds for itself, such as `area: …`, are left alone.
set -eu

repo=${1:?usage: sync.sh OWNER/REPO [--prune]}
here=$(dirname "$0")

python3 - "$here/labels.json" <<'PY' | while IFS="$(printf '\t')" read -r name color description; do
import json, sys
for label in json.load(open(sys.argv[1])):
    print(label["name"], label["color"], label["description"], sep="\t")
PY
  gh label create "$name" --repo "$repo" --color "$color" --description "$description" --force
done

if [ "${2:-}" = "--prune" ]; then
  for name in bug enhancement documentation question invalid wontfix; do
    gh label delete "$name" --repo "$repo" --yes 2>/dev/null || true
  done
fi
