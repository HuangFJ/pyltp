#!/bin/bash

PY=python

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then

    # Install some custom requirements on OS X
    # e.g. brew install pyenv-virtualenv
    brew update > /dev/null
    case "${TOXENV}" in
        py2)
            brew install python
            ;;
        py3)
            brew install python3
            PY=python3
            ;;
    esac
else
    # Install some custom requirements on Linux
    echo "";
fi

$PY --version
$PY setup.py install
