#!/usr/bin/env python3
"""Train LiLa-E8 on spool data with GPU"""
import sys
sys.path.insert(0, '.')
from config.config import E8Config
import torch
from pathlib import Path

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"🔬 Training on {device}")

# Load checkpoint
checkpoint = torch.load('checkpoint_step_200000.pt', map_location=device, weights_only=False)
print(f"✅ Loaded checkpoint (step {checkpoint['step']}, loss {checkpoint['loss']:.4f})")

# Collect spool data
spool_path = Path("/mnt/data1/spool")
docs_path = Path.home() / "DOCS"

files = []
if spool_path.exists():
    files.extend(list(spool_path.rglob("*.txt"))[:50])
    files.extend(list(spool_path.rglob("*.md"))[:50])
if docs_path.exists():
    files.extend(list(docs_path.rglob("*.md"))[:50])

print(f"📂 Found {len(files)} files for training")
print(f"✅ Training data ready on {device}")
