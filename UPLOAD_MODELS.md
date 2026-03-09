# Model Upload Guide

## Hugging Face

### 1. Login

```bash
pip install huggingface_hub
huggingface-cli login
```

### 2. Upload Models

```bash
cd /mnt/data1/time-2026/03-march/09/lila-e8-clean
python scripts/upload_to_hf.py
```

This will upload 3 models:
- `meta-introspector/lila-e8-monster-stories`
- `meta-introspector/lila-e8-time2026`
- `meta-introspector/lila-e8-fandom-multiverse`

## Google Colab

Create notebook with:

```python
!pip install sentencepiece torch
!git clone https://github.com/meta-introspector/sovereign-lila-e8.git
%cd sovereign-lila-e8

# Download model from HF
from huggingface_hub import hf_hub_download
checkpoint = hf_hub_download(
    repo_id="meta-introspector/lila-e8-monster-stories",
    filename="checkpoint_step_51000.pt"
)

# Run inference
!python scripts/run_inference.py --checkpoint {checkpoint} --prompt "Once upon a time"
```

## Kaggle

1. Upload checkpoint as Kaggle Dataset
2. Create notebook:

```python
import sys
sys.path.append('/kaggle/input/sovereign-lila-e8')

import torch
from model.lila_e8 import LilaE8

checkpoint = torch.load('/kaggle/input/lila-e8-monster/checkpoint_step_51000.pt')
model = LilaE8(checkpoint['config'])
model.load_state_dict(checkpoint['model_state_dict'])
```

## Model Sizes

- Monster: 51 checkpoints × 479MB = ~24GB
- Time2026: 22 checkpoints × 479MB = ~10GB  
- Multiverse: 23 checkpoints × 479MB = ~11GB

**Recommendation**: Upload only latest checkpoint per model (~1.4GB total)
