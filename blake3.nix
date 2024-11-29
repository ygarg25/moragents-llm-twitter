{
    lib,
    buildPythonPackage,
    fetchurl,
}:

buildPythonPackage rec {
    pname = "blake3";
    version = "0.4.1";
    format = "wheel";

    src = fetchurl {
        url = "https://files.pythonhosted.org/packages/ad/9e/84fda33f9cd0b978d9e73becf51f3e11e33180e07e5b6bf3d16fbc4021e2/blake3-0.4.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl";
        sha256 = "d653623361da8db3406f4a90b39d38016f9f678e22099df0d5f8ab77efb7b4ae";
    };

    pythonImportsCheck = [
        "blake3"
    ];
}
