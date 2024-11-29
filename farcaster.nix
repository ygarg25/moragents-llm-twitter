{
    lib,
    buildPythonPackage,
    fetchPypi,
    poetry-core,
    python-dotenv,
    pydantic,
    pyhumps,
    requests,
    canonicaljson,
    eth-account,
    parsimonious,
    setuptools,
}:

buildPythonPackage rec {
    pname = "farcaster";
    version = "0.7.11";
    #   format = "pyproject";

    src = fetchPypi {
        inherit pname version;
        hash = "sha256:45746e3d1718bed6dd231764da0ad5805f643a23e1a4a07907a8970c4e28e6bf";
    };

    dependencies = [
        python-dotenv
        pydantic
        pyhumps
        requests
        canonicaljson
        eth-account
        parsimonious
    ];

    # TODO: check this after removing the override for parsimonious 0.9.0
    # postPatch = ''
    # substituteInPlace pyproject.toml \
    #     --replace 'parsimonious = ">=0.8.1,<0.10.0"' "parsimonious"
    # '';

    # do not run tests
    doCheck = false;

    pythonImportsCheck = [
        "farcaster"
    ];

    # specific to buildPythonPackage, see its reference
    pyproject = true;
    build-system = [
        poetry-core
        setuptools
    ];
}
