#!/bin/bash
# Start all parallel training sessions

cd /mnt/data1/time-2026/03-march/09/lila-e8-clean

echo "🚀 Starting Parallel Training"
echo "=============================="
echo ""

# Already running: Monster (session: lila-train)
echo "1. Monster stories - Already running (lila-train)"

# Start Time-2026
./scripts/train_time2026.sh
sleep 2

# Start Multiverse
./scripts/train_multiverse.sh
sleep 2

echo ""
echo "📊 Active Sessions:"
tmux list-sessions | grep lila

echo ""
echo "💾 GPU Status:"
nvidia-smi --query-gpu=utilization.gpu,memory.used,memory.total --format=csv,noheader

echo ""
echo "Commands:"
echo "  tmux attach -t lila-train       # Monster"
echo "  tmux attach -t lila-time2026    # Time-2026"
echo "  tmux attach -t lila-multiverse  # Multiverse"
echo "  watch -n 5 nvidia-smi           # Monitor GPU"
