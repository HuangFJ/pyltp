#!/bin/bash

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then

    # Install some custom requirements on OS X
    # e.g. brew install pyenv-virtualenv

    case "${TOXENV}" in
        py27)
            # Install some custom Python 3.2 requirements on OS X
            ;;
        py35)
            # Install some custom Python 3.3 requirements on OS X
            ;;
    esac
else
    # Install some custom requirements on Linux
    echo "";
fi

export PYLTPVER=$(python setup.py --version)
python setup.py build
python setup.py sdist
cd dist/
tar zxvf pyltp-$PYLTPVER.tar.gz > /dev/null
cd pyltp-$PYLTPVER
python setup.py build >& /dev/null
cd ../../
mkdir -p lib/
cp build/lib.*/pyltp.so lib
