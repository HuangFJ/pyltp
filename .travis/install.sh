#!/bin/bash

PY=python

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then

    # Install some custom requirements on OS X
    # e.g. brew install pyenv-virtualenv
    brew update
    case "${TOXENV}" in
        py2)
            brew install python
            ;;
        py3)
            brew install python3
            PY = python3
            ;;
    esac
else
    # Install some custom requirements on Linux
    echo "";
fi

export PYLTPVER=$(${PY} setup.py --version)
$PY setup.py build
$PY setup.py sdist
cd dist/
tar zxvf pyltp-$PYLTPVER.tar.gz > /dev/null
cd pyltp-$PYLTPVER
$PY setup.py build >& /dev/null
cd ../../
mkdir -p lib/
ls .
ls build
ls build/lib.*/
cp build/lib.*/pyltp.so lib
