# Training Lila-E8 on Monster Stories

**Date**: 2026-03-09
**Location**: `/mnt/data1/time-2026/03-march/09/lila-e8-clean`
**Dataset**: Monster stories (340 stories, 79KB)

## Setup

```bash
# Clone fresh upstream
cd /mnt/data1/time-2026/03-march/09
git clone https://github.com/SPUTNIKAI/sovereign-lila-e8.git lila-e8-clean
cd lila-e8-clean

# Symlink Monster stories dataset
mkdir -p data
ln -s /mnt/data1/time-2026/03-march/07/monster-ngram-learning/data/monster_stories_with_proof.txt data/monster_stories.txt

# Verify nix environment
nix develop --impure --command python -c "import torch; print('✓ PyTorch', torch.__version__)"
```

## Training Command

```bash
cd /mnt/data1/time-2026/03-march/09/lila-e8-clean
nix develop --impure --command python scripts/train_model.py \
  --checkpoint_dir checkpoints/monster 2>&1 | tee training.log
```

## What It Does

1. Downloads TinyStories dataset (first run)
2. Initializes Lila-E8 model with E8 geometry
3. Trains on TinyStories (default behavior)
4. Saves checkpoints to `checkpoints/monster/`

## To Use Monster Stories

The default script trains on TinyStories. To train on Monster stories, we need to modify the training script or create a custom one.

## Status

- ⏳ Training interrupted (user cancelled)
- ✅ Environment working (PyTorch 2.5.1+cu121, CUDA available)
- ✅ Dataset symlinked
- ⏳ Need to configure training to use Monster stories

## Next Steps

1. Check how training.train() loads data
2. Modify to use data/monster_stories.txt
3. Start training
4. Monitor loss convergence
