#!/usr/bin/env python3
import torch
from config.config import E8Config
from models.model import E8GPT

config = E8Config(vocab_size=2048, d_model=128, n_layers=2, n_heads=4, block_size=64)
model = E8GPT(config)
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)

x = torch.randint(0, 2048, (2, 64))
y = torch.randint(0, 2048, (2, 64))

logits, loss = model(x, y)
loss.backward()
optimizer.step()

print(f"✓ Training step completed, loss: {loss.item():.4f}")
