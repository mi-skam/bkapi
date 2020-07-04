{ pkgs ? import <nixpkgs> {} }:
let
  requirements = import ./requirements.nix { inherit pkgs; };
in
pkgs.python38Packages.buildPythonApplication rec {
  name = "bkapi";
  version = "1.0.0";
  namePrefix = "";
  src = ./.;
  doCheck = false;
  propagatedBuildInputs = builtins.attrValues requirements.packages;
}