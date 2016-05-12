#!/usr/bin/env python
import glob
import os
import sys
import codecs
from setuptools import setup, Extension

ltp_root="ltp"
ltp_source=os.path.join(ltp_root, "src")
ltp_thirdparty=os.path.join(ltp_root, "thirdparty")
patch_root="patch"
patch_libs=os.path.join(patch_root, "libs", "python", "src")

excluded_sources = (
        os.path.join(ltp_source, "segmentor", "otcws.cpp"),
        os.path.join(ltp_source, "segmentor", "io.cpp"),
        os.path.join(ltp_source, "segmentor", "segmentor_frontend.cpp"),
        os.path.join(ltp_source, "segmentor", "customized_segmentor_frontend.cpp"),
        os.path.join(ltp_source, "postagger", "otpos.cpp"),
        os.path.join(ltp_source, "postagger", "io.cpp"),
        os.path.join(ltp_source, "postagger", "postagger_frontend.cpp"),
        os.path.join(ltp_source, "ner", "otner.cpp"),
        os.path.join(ltp_source, "ner", "io.cpp"),
        os.path.join(ltp_source, "ner", "ner_frontend.cpp"),
        os.path.join(ltp_source, "parser.n", "main.cpp"),
        os.path.join(ltp_source, "parser.n", "io.cpp"),
        os.path.join(ltp_source, "parser.n", "parser_frontend.cpp"),
        os.path.join(ltp_source, "srl", "lgsrl.cpp"),
        os.path.join(ltp_thirdparty, "maxent", "train.cpp"),
        os.path.join(ltp_thirdparty, "maxent", "predict.cpp")
        )

sources = [os.path.join("src", "pyltp.cpp")]
sources += glob.glob(os.path.join(ltp_thirdparty, "boost", "libs", "regex", "src", "*.cpp"))
sources += glob.glob(os.path.join(ltp_thirdparty, "maxent", "*.cpp"))
sources += glob.glob(os.path.join(ltp_source, "splitsnt", "*.cpp"))
sources += glob.glob(os.path.join(ltp_source, "segmentor", "*.cpp"))
sources += glob.glob(os.path.join(ltp_source, "postagger", "*.cpp"))
sources += glob.glob(os.path.join(ltp_source, "ner", "*.cpp"))
sources += glob.glob(os.path.join(ltp_source, "parser.n", "*.cpp"))
sources += glob.glob(os.path.join(ltp_source, "srl", "*.cpp"))
sources += glob.glob(os.path.join(patch_libs, "*.cpp"))
sources += glob.glob(os.path.join(patch_libs, "object", "*.cpp"))
sources += glob.glob(os.path.join(patch_libs, "converter", "*.cpp"))

sources = [source for source in sources if source not in excluded_sources]

includes = [
        'ltp/include/',
        'ltp/thirdparty/boost/include/',
        'ltp/thirdparty/eigen-3.2.4',
        'ltp/thirdparty/maxent/',
        'ltp/src/',
        'ltp/src/splitsnt',
        'ltp/src/segmentor/',
        'ltp/src/postagger/',
        'ltp/src/ner/',
        'ltp/src/parser.n/',
        'ltp/src/srl/',
        'ltp/src/utils/',
        'ltp/src/srl/',
        'patch/include/'
        ]

extra_compile_args = []

if sys.platform == 'win32':
    extra_compile_args += ['/DBOOST_PYTHON_SOURCE', '/DBOOST_PYTHON_STATIC_LIB', '/EHsc']
elif sys.platform == 'darwin':
    os.environ['CC'] = 'clang++'
    os.environ['CXX'] = 'clang++'
    extra_compile_args += ['-std=c++11', '-Wno-c++11-narrowing', '-stdlib=libc++']
else:
    extra_compile_args += ['-std=c++0x']

ext_modules = [Extension('pyltp',
    include_dirs=includes,
    language='c++',
    sources=sources,
    extra_compile_args=extra_compile_args
    )]

setup(
    name='pyltp',
    version='0.1.9.1',
    description='pyltp: the python extension for LTP',
    long_description=codecs.open('README.md', encoding='utf-8').read(),
    author='Yijia Liu, Zixiang Xu',
    author_email='ltp-cloud@googlegroups.com',
    url='https://github.com/HIT-SCIR/pyltp',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing :: Linguistic",
    ],
    zip_safe=False,
    #packages=['pyltp'],
    ext_modules=ext_modules
)
