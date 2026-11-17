#!/usr/bin/env bash
# Prints the query string that gives a shields.io badge a project's icon and
# colours. Append it to any shields.io badge address.
#
#   brand/tools/shield.sh PROJECT        e.g. hatchery
set -euo pipefail
cd "$(dirname "$0")/.."
project=${1:?usage: shield.sh PROJECT}
case $project in
  aiviarium) colour=3FCF8E ;;
  rookery) colour=F2B33D ;;
  parrot) colour=FF6369 ;;
  crow) colour=8F8FFA ;;
  hatchery) colour=E879F9 ;;
  *) echo "error: unknown project $project" >&2; exit 1 ;;
esac
logo=$(tr -s ' \n' ' ' < "icons/$project-icon.svg" | sed 's/> </></g; s/ $//' | base64 -w0 | sed 's/+/%2B/g; s/\//%2F/g; s/=/%3D/g')
echo "style=flat&labelColor=18181B&color=$colour&logo=data:image/svg%2Bxml;base64,$logo"
