with import <nixpkgs> { };

stdenv.mkDerivation {
  name = "python-env";
  nativeBuildInputs = [
    python3
    python3Packages.numpy
    python3Packages.pandas
    python3Packages.scipy
    python3Packages.matplotlib
  ];
}
