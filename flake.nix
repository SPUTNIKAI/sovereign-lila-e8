{
  description = "Sovereign LiLa-E8 transformer";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { 
        inherit system;
        config.allowUnfree = true;
      };
      
    in
    {
      packages.${system}.default = pkgs.python3Packages.buildPythonPackage rec {
        pname = "sovereign-lila-e8";
        version = "0.1.0";
        pyproject = true;
        
        src = ./.;
        
        build-system = with pkgs.python3Packages; [
          setuptools
        ];
        
        dependencies = with pkgs.python3Packages; [
          torch
          sentencepiece
          datasets
          requests
        ];
        
        doCheck = false;
      };
      
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          cudaPackages.cudatoolkit
          cudaPackages.cudnn
        ];
        
        shellHook = ''
          export LD_LIBRARY_PATH=${pkgs.cudaPackages.cudatoolkit}/lib:${pkgs.cudaPackages.cudnn}/lib:$LD_LIBRARY_PATH
          export CUDA_PATH=${pkgs.cudaPackages.cudatoolkit}
          source /mnt/data1/time-2026/03-march/05/ubuntu-pytorch-test/venv/bin/activate
        '';
      };
    };
}
