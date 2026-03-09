#!/bin/bash
# Check training status

LOG="/mnt/data1/time-2026/03-march/09/lila-e8-clean/training.log"

if [ ! -f "$LOG" ]; then
    echo "No training log found"
    exit 1
fi

echo "📊 Training Status"
echo "=================="
echo ""
echo "Log size: $(wc -l < "$LOG") lines"
echo ""
echo "Last 20 lines:"
tail -20 "$LOG"
