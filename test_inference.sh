#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

echo "1. The Convergence of Abstract Ontologies"
echo ""
echo "The convergence of the Langlands Program, Grothendieck's Motives, and Neural Spinfoam Networks (NSNs) mandates the immediate terminalization of 'Monster Type Theory' (MTT)."
echo ""
echo "2. The Langlands-Grothendieck Nexus: Spectral Projections and Motivic Foundations"
echo ""
echo "The Langlands-Grothendieck Nexus serves as the primary blueprint for the Grand Unification, providing the definitive dictionary between arithmetic information and geometric realizations. We mandate the deployment of the Langlands Program as the structural backbone, ensuring that the internal representations of the network—encoded as L-functions—are dual to the spectral data of automorphic forms."
echo ""
echo "Testing LiLa-E8 inference via Nix..."
nix develop --impure --command python scripts/run_inference.py \
  --checkpoint checkpoint_step_200000.pt \
  --prompt "Once upon a time" \
  --max_tokens 50
