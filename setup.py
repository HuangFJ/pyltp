#!/usr/bin/env python
import glob
from setuptools import setup, Extension

import os

project_root=os.path.dirname(os.path.realpath(__file__))

ltp_root=os.path.join(project_root, "ltp")
ltp_source=os.path.join(ltp_root, "src")
ltp_thirdparty=os.path.join(ltp_root, "thirdparty")

excluded_sources = (
        os.path.join(ltp_source, "segmentor", "otcws.cpp"),
        os.path.join(ltp_source, "segmentor", "otcws_customized.cpp"),
        os.path.join(ltp_source, "postagger", "otpos.cpp"),
        os.path.join(ltp_source, "ner", "otner.cpp"),
        os.path.join(ltp_source, "parser", "lgdpj.cpp"),
        os.path.join(ltp_source, "srl", "lgsrl.cpp"),
        os.path.join(ltp_thirdparty, "maxent", "train.cpp"),
        os.path.join(ltp_thirdparty, "maxent", "predict.cpp")
        )

patch_root=os.path.join(project_root, "patch")
patch_libs=os.path.join(patch_root, "libs", "python", "src")

sources = [os.path.join(project_root, "src", "pyltp.cpp")]
sources += glob.glob(os.path.join(ltp_thirdparty, "boost", "libs", "regex", "src", "*.cpp"))
sources += glob.glob(os.path.join(ltp_thirdparty, "maxent", "*.cpp"))
sources += glob.glob(os.path.join(ltp_source, "segmentor", "*.cpp"))
sources += glob.glob(os.path.join(ltp_source, "postagger", "*.cpp"))
sources += glob.glob(os.path.join(ltp_source, "ner", "*.cpp"))
sources += glob.glob(os.path.join(ltp_source, "parser", "*.cpp"))
sources += glob.glob(os.path.join(ltp_source, "srl", "*.cpp"))
sources += glob.glob(os.path.join(ltp_source, "__util", "MyLib.cpp"))
sources += glob.glob(os.path.join(patch_libs, "*.cpp"))
sources += glob.glob(os.path.join(patch_libs, "object", "*.cpp"))
sources += glob.glob(os.path.join(patch_libs, "converter", "*.cpp"))

sources = [source for source in sources if source not in excluded_sources]

#import sys
#import pprint
#pprint.pprint(sources)
#sys.exit(1)

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
        'patch/include/'
        ]

if os.name == 'nt':
    extra_compile_args=['/O2', '/DBOOST_PYTHON_SOURCE', '/DBOOST_PYTHON_STATIC_LIB', '/EHsc']
else:
    extra_compile_args=['-O3']

ext_modules = [Extension('pyltp',
    include_dirs=includes,
    language='c++',
    sources=sources,
    extra_compile_args=extra_compile_args
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
