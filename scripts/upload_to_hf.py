#!/usr/bin/env python3
"""Upload trained Lila-E8 models to Hugging Face"""

from huggingface_hub import HfApi, create_repo
import os
import glob

# Initialize API
api = HfApi()

# Model info
models = {
    'monster': {
        'name': 'lila-e8-monster-stories',
        'description': 'Lila-E8 trained on Monster Group TinyStories (340 stories)',
        'checkpoints': 'checkpoints/monster/',
        'tags': ['monster-group', 'e8-geometry', 'tinystories']
    },
    'time2026': {
        'name': 'lila-e8-time2026',
        'description': 'Lila-E8 trained on Time-2026 temporal lattice stories',
        'checkpoints': 'checkpoints/time2026/',
        'tags': ['temporal-lattice', 'e8-geometry', 'tinystories']
    },
    'multiverse': {
        'name': 'lila-e8-fandom-multiverse',
        'description': 'Lila-E8 trained on Fandom Multiverse (Monster + Time2026 + LMFDB + MathJax)',
        'checkpoints': 'checkpoints/multiverse/',
        'tags': ['multiverse', 'e8-geometry', 'tinystories', 'mathematical-narratives']
    }
}

def upload_model(model_key, model_info, username="h4"):
    """Upload a model to Hugging Face"""
    
    repo_id = f"{username}/{model_info['name']}"
    
    print(f"\n📦 Uploading {model_key}...")
    print(f"   Repo: {repo_id}")
    
    # Create repo
    try:
        create_repo(repo_id, repo_type="model", exist_ok=True)
        print(f"   ✓ Repo created/exists")
    except Exception as e:
        print(f"   ✗ Error creating repo: {e}")
        return
    
    # Find latest checkpoint
    checkpoints = sorted(glob.glob(f"{model_info['checkpoints']}/checkpoint_step_*.pt"))
    if not checkpoints:
        print(f"   ✗ No checkpoints found")
        return
    
    latest = checkpoints[-1]
    step = os.path.basename(latest).replace('checkpoint_step_', '').replace('.pt', '')
    
    print(f"   Latest checkpoint: step {step}")
    
    # Upload checkpoint
    try:
        api.upload_file(
            path_or_fileobj=latest,
            path_in_repo=f"checkpoint_step_{step}.pt",
            repo_id=repo_id,
            repo_type="model"
        )
        print(f"   ✓ Uploaded checkpoint")
    except Exception as e:
        print(f"   ✗ Error uploading: {e}")
        return
    
    # Create model card
    card = f"""---
tags:
{chr(10).join(f'- {tag}' for tag in model_info['tags'])}
license: agpl-3.0
---

# {model_info['name']}

{model_info['description']}

## Model Details

- **Architecture**: Lila-E8 (Lie Lattice Attention)
- **E8 Quantization**: 240 roots
- **Geometric Attention**: E8-biased
- **Training Steps**: {step}
- **Framework**: PyTorch

## Usage

```python
import torch
from model.lila_e8 import LilaE8Config, LilaE8

# Load checkpoint
checkpoint = torch.load('checkpoint_step_{step}.pt', map_location='cpu')
config = checkpoint['config']
model = LilaE8(config)
model.load_state_dict(checkpoint['model_state_dict'])

# Generate
# (see inference examples in repo)
```

## Training

Trained on NVIDIA RTX 3080 Ti using Nix reproducible environment.

See [sovereign-lila-e8](https://github.com/meta-introspector/sovereign-lila-e8) for training code.
"""
    
    try:
        api.upload_file(
            path_or_fileobj=card.encode(),
            path_in_repo="README.md",
            repo_id=repo_id,
            repo_type="model"
        )
        print(f"   ✓ Uploaded model card")
    except Exception as e:
        print(f"   ✗ Error uploading card: {e}")
    
    print(f"   🔗 https://huggingface.co/{repo_id}")

if __name__ == "__main__":
    print("🚀 Uploading Lila-E8 Models to Hugging Face")
    print("=" * 60)
    
    # Check login
    try:
        api.whoami()
        print("✓ Logged in to Hugging Face")
    except:
        print("✗ Not logged in. Run: huggingface-cli login")
        exit(1)
    
    # Upload each model
    for key, info in models.items():
        upload_model(key, info)
    
    print("\n✅ Upload complete!")
