#!/usr/bin/env bash
# Writes the badges every project uses into brand/badges. Run it after a
# change to badge.py, to an icon, or to a project's state.
set -euo pipefail
cd "$(dirname "$0")/.."
badge() { python3 tools/badge.py "$@"; }

for project in aiviarium rookery parrot crow hatchery; do
  name=${project^}
  badge "$project" "$name" -o "badges/$project.svg"
  [ "$project" = aiviarium ] || badge aiviarium Aiviarium "$name" --value-colour "$project" -o "badges/$project-family.svg"
done

badge rookery state "moving here" -o badges/rookery-state.svg
badge parrot state "moving here" -o badges/parrot-state.svg
badge crow state "not public yet" -o badges/crow-state.svg
badge hatchery state "in development" -o badges/hatchery-state.svg

for project in rookery parrot hatchery; do
  badge "$project" license "MIT OR Apache-2.0" -o "badges/$project-license.svg"
done
