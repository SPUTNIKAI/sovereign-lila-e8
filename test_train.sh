#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

echo "3. Neural Spinfoam Networks: The Quantum Geometry of Attention"
echo ""
echo "Testing LiLa-E8 training on spool data via Nix..."
nix develop --impure --command python test_train.py
