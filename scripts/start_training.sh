#!/bin/bash
# Train Lila-E8 on TinyStories in tmux session

cd /mnt/data1/time-2026/03-march/09/lila-e8-clean

# Create tmux session
tmux new-session -d -s lila-train

# Run training
tmux send-keys -t lila-train "cd /mnt/data1/time-2026/03-march/09/lila-e8-clean" C-m
tmux send-keys -t lila-train "nix develop --impure --command python scripts/train_model.py --checkpoint_dir checkpoints/monster 2>&1 | tee training.log" C-m

echo "✓ Training started in tmux session 'lila-train'"
echo ""
echo "Commands:"
echo "  tmux attach -t lila-train    # Attach to session"
echo "  tmux detach                  # Detach (Ctrl+b d)"
echo "  tail -f training.log         # Monitor log"
echo "  tmux kill-session -t lila-train  # Stop training"
