#!/bin/bash
# Train on Time-2026 dataset in tmux

cd /mnt/data1/time-2026/03-march/09/lila-e8-clean

tmux new-session -d -s lila-time2026
tmux send-keys -t lila-time2026 "cd /mnt/data1/time-2026/03-march/09/lila-e8-clean" C-m
tmux send-keys -t lila-time2026 "nix develop --impure --command python scripts/train_model.py --checkpoint_dir checkpoints/time2026 2>&1 | tee training_time2026.log" C-m

echo "✓ Training Time-2026 started in tmux session 'lila-time2026'"
