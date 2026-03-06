{
  description = "Sovereign LiLa-E8 transformer";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = import nixpkgs { inherit system; };
      
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
    };
}
