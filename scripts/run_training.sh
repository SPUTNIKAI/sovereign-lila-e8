#!/bin/bash
# Run training directly and capture output

cd /mnt/data1/time-2026/03-march/09/lila-e8-clean

echo "🚀 Starting Lila-E8 Training"
echo "=============================="
echo ""

nix develop --impure --command python scripts/train_model.py --checkpoint_dir checkpoints/monster 2>&1 | tee training.log
