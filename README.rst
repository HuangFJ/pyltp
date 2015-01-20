===================================
pyltp: the python extension for LTP
===================================

|Pypi Status| |Build Status|

pyltp是\ `语言技术平台(Language Technology Platform,LTP) <https://github.com/HIT-SCIR/ltp>`__\ 的Python封装。
关于LTP更多的信息，欢迎访问LTP项目主页。

简介与背景知识
==============

pyltp是\ `语言技术平台(Language Technology Platform,LTP) <https://github.com/HIT-SCIR/ltp>`__\ 接口的一个Python封装。
本项目旨在使Python用户可以本地调用LTP。
该项目还处于测试状态，欢迎反馈bug。

在使用pyltp之前，您需要简要了解

* `什么是语言技术平台 <https://github.com/HIT-SCIR/ltp/blob/master/doc/ltp-document-3.0.md#%E7%AE%80%E4%BB%8B>`__\ ，它能否帮助您解决问题
* `如何安装语言技术平台 <https://github.com/HIT-SCIR/ltp/blob/master/doc/ltp-document-3.0.md#%E5%A6%82%E4%BD%95%E5%AE%89%E8%A3%85ltp>`__
* `语言技术平台提供哪些编程接口 <https://github.com/HIT-SCIR/ltp/blob/master/doc/ltp-document-3.0.md#%E7%BC%96%E7%A8%8B%E6%8E%A5%E5%8F%A3>`__

如果您对这些问题不了解，请首先阅读我们提供的有关语言技术平台的文档。
在本文档的后续中，我们假定您已经阅读并成功编译并使用语言技术平台。

安装
====

现阶段，pyltp主要在Linux编译测试。我们也欢迎用户提供其他平台的测试结果。

pypi安装

::

    $ pip install pyltp

如果您使用使用github的开发版的pyltp，您可以采用如下命令编译pyltp

::

    $ git clone https://github.com/HIT-SCIR/pyltp
    $ git submodule init
    $ git submodule update
    $ python setup.py build

例子
====

::

    # -*- coding: utf-8 -*-
    from pyltp import Segmentor
    segmentor = Segmentor()
    segmentor.load("/path/to/your/cws/model")
    words = segmentor.segment("元芳你怎么看")
    print "|".join(words)

更多例子，请参考\ `example/example.py <https://github.com/HIT-SCIR/pyltp/blob/master/example/example.py>`__\

作者
====

-  徐梓翔 << zxxu@ir.hit.edu.cn >> 2015-01-20 解决跨平台运行问题
-  刘一佳 << yjliu@ir.hit.edu.cn >> 2014-06-12 重组项目
-  HuangFJ << biohfj@gmail.com >> 本项目最初作者

.. |Pypi Status| image:: https://pypip.in/v/pyltp/badge.png
   :target: https://pypi.python.org/pypi/pyltp

.. |Build Status| image:: https://travis-ci.org/HIT-SCIR/pyltp.svg?branch=master
   :target: https://travis-ci.org/HIT-SCIR/pyltp
