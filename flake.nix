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
      
      torch-wheel = pkgs.fetchurl {
        url = "https://download.pytorch.org/whl/cu121/torch-2.5.1%2Bcu121-cp313-cp313-linux_x86_64.whl";
        sha256 = "0jzxdwymh0wmqykw00jg71gww8a6z31ncyi5hf9vxy8gkfviizhv";
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
          python3
          cudaPackages.cudatoolkit
          cudaPackages.cudnn
        ];
        
        shellHook = ''
          export LD_LIBRARY_PATH=${pkgs.lib.makeLibraryPath [
            pkgs.zlib
            pkgs.cudaPackages.cudatoolkit
            pkgs.cudaPackages.cudnn
          ]}:$LD_LIBRARY_PATH
          export CUDA_PATH=${pkgs.cudaPackages.cudatoolkit}
          
          # Use the working venv
          source /mnt/data1/time-2026/03-march/05/ubuntu-pytorch-test/venv/bin/activate
        '';
      };
    };
}
