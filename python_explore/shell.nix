with import <nixpkgs> { };

stdenv.mkDerivation {
  name = "python-env";
  nativeBuildInputs = [
    python3
    python3Packages.pip
    python3Packages.numpy
    python3Packages.pandas
    python3Packages.scipy
    python3Packages.matplotlib
  ];
  # for python packages with C++ extensions need to add the following hack
  NIX_CFLAGS_COMPILE = pkgs.lib.optionals pkgs.stdenv.isDarwin [
    "-I${pkgs.lib.getDev pkgs.libcxx}/include/c++/v1"
  ];
}
