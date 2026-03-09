# GitHub Actions CI/CD

## Workflows

### 1. Test Nix Build (`.github/workflows/test-nix.yml`)

Tests that the Nix flake works correctly:
- ✅ Flake check passes
- ✅ Development shell loads
- ✅ PyTorch imports
- ✅ SentencePiece available
- ✅ Model imports successfully

### 2. Test Training Setup (`.github/workflows/test-training.yml`)

Tests parallel training infrastructure:
- ✅ All training scripts present
- ✅ Scripts are executable
- ✅ Python syntax valid
- ✅ Documentation exists

## Security

All actions use `meta-introspector/*` namespace for security:
- `meta-introspector/checkout@v4`
- `meta-introspector/install-nix-action@v26`

## Triggers

Both workflows run on:
- Push to `main` branch
- Pull requests to `main` branch

## Local Testing

Test the same checks locally:

```bash
# Test Nix flake
nix flake check --impure

# Test development shell
nix develop --impure --command python -c "import torch; print('OK')"

# Test model import
nix develop --impure --command python -c "from model.lila_e8 import LilaE8Config; print('OK')"

# Check scripts exist
ls -l scripts/*.sh

# Verify documentation
ls -l *.md
```

## Expected Results

All checks should pass:
- ✅ Nix flake builds
- ✅ Dependencies available
- ✅ Scripts present and executable
- ✅ Documentation complete

## Adding New Tests

To add new tests, edit the workflow files:
- `.github/workflows/test-nix.yml` - Nix/build tests
- `.github/workflows/test-training.yml` - Training infrastructure tests

Follow the existing pattern using `meta-introspector/*` actions.
