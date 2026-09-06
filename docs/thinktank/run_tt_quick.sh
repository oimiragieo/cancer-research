#!/usr/bin/env bash
set -euo pipefail
Q="/mnt/c/dev/projects/cancer-research/.claude/thinktank_cancer-ralph-design.md"
OUT="/mnt/c/dev/projects/cancer-research/docs/thinktank/cancer-ralph-design"
mkdir -p "$OUT"
export SEAT1_MODEL="${SEAT1_MODEL:-sonnet}"
export TT_TIMEOUT="${TT_TIMEOUT:-300}"
export TT_MIN_VERDICTS="${TT_MIN_VERDICTS:-2}"
export SEATS="${SEATS:-codex agy}"
if [[ -x /mnt/c/Users/oimir/bin/droid.exe ]]; then
  export DROID=/mnt/c/Users/oimir/bin/droid.exe
fi
echo "Q=$Q"
echo "OUT=$OUT"
echo "SEATS=$SEATS"
bash /mnt/c/Users/oimir/.claude/skills/use-thinktank/tt_council.sh "$Q" "$OUT"
