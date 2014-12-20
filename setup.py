#!/usr/bin/env python
import glob
from setuptools import setup, Extension

excluded_sources = (
        'ltp/src/segmentor/otcws.cpp',
        'ltp/src/segmentor/otcws_customized.cpp',
        'ltp/src/postagger/otpos.cpp',
        'ltp/src/ner/otner.cpp',
        'ltp/src/parser/lgdpj.cpp',
        'ltp/src/srl/lgsrl.cpp',
        'ltp/thirdparty/maxent/train.cpp',
        'ltp/thirdparty/maxent/predict.cpp')

sources = ['src/pyltp.cpp']
sources += glob.glob('ltp/thirdparty/boost/libs/regex/src/*.cpp')
sources += glob.glob('ltp/thirdparty/maxent/*.cpp')
sources += glob.glob('ltp/src/segmentor/*.cpp') 
sources += glob.glob('ltp/src/postagger/*.cpp')
sources += glob.glob('ltp/src/ner/*.cpp')
sources += glob.glob('ltp/src/parser/*.cpp')
sources += glob.glob('ltp/src/srl/*.cpp')
sources += glob.glob('ltp/src/__util/MyLib.cpp')
sources += glob.glob('boost_python/src/*.cpp')
sources += glob.glob('boost_python/src/object/*.cpp')
sources += glob.glob('boost_python/src/converter/*.cpp')

sources = [source for source in sources if source not in excluded_sources]

includes = [
        'ltp/include/',
        'ltp/thirdparty/boost/include/',
        'ltp/thirdparty/maxent/',
        'ltp/src/',
        'ltp/src/segmentor/',
        'ltp/src/postagger/',
        'ltp/src/ner/',
        'ltp/src/parser',
        'ltp/src/srl/',
        'ltp/src/utils/',
        'ltp/src/__util/',
        'ltp/src/srl/',
        'boost_python/include/'
        ]

ext_modules = [Extension('pyltp',
    include_dirs=includes,
    language='c++',
    sources=sources
    )]

setup(
    name='pyltp',
    version='0.1.1',
    description='pyltp: the python extension for LTP',
    long_description=open('README.rst').read(),
    author='Yijia Liu',
    author_email='ltp-cloud@googlegroups.com',
    url='https://github.com/HIT-SCIR/pyltp',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    zip_safe=False,
    #packages=['pyltp'],
    ext_modules=ext_modules
)
