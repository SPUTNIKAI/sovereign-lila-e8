#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
nix develop --impure --command python inference/generate.py "$@"
