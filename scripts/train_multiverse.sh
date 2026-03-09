#!/bin/bash
# Train on Fandom Multiverse dataset in tmux

cd /mnt/data1/time-2026/03-march/09/lila-e8-clean

tmux new-session -d -s lila-multiverse
tmux send-keys -t lila-multiverse "cd /mnt/data1/time-2026/03-march/09/lila-e8-clean" C-m
tmux send-keys -t lila-multiverse "nix develop --impure --command python scripts/train_model.py --checkpoint_dir checkpoints/multiverse 2>&1 | tee training_multiverse.log" C-m

echo "✓ Training Fandom Multiverse started in tmux session 'lila-multiverse'"
