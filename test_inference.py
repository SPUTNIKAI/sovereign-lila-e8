#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
from config.config import E8Config
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")

checkpoint = torch.load('checkpoint_step_200000.pt', map_location=device, weights_only=False)
print(f"✅ Loaded checkpoint (step {checkpoint['step']}, loss {checkpoint['loss']:.4f})")
print(f"✅ Inference ready on {device}")
