#!/bin/bash
# Monitor Lila-E8 training

LOG_FILE="/mnt/data1/time-2026/03-march/09/lila-e8-clean/training.log"

echo "🔍 Monitoring Lila-E8 Training"
echo "=============================="
echo ""

# Check if training is running
if tmux has-session -t lila-train 2>/dev/null; then
    echo "✓ Training session active"
else
    echo "✗ No training session found"
    exit 1
fi

# Show recent log
if [ -f "$LOG_FILE" ]; then
    echo "📊 Recent output:"
    echo "----------------"
    tail -30 "$LOG_FILE"
    echo ""
    echo "📈 Training stats:"
    grep -E "(step|loss|val)" "$LOG_FILE" | tail -10
else
    echo "⏳ Waiting for log file..."
fi

echo ""
echo "Commands:"
echo "  tail -f $LOG_FILE"
echo "  tmux attach -t lila-train"
