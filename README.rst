===================================
pyltp: the python extension for LTP
===================================

|Pypi Status| |Build Status|

pyltp是\ `语言技术平台(Language Technology Platform, LTP) <https://github.com/HIT-SCIR/ltp>`__\ 的Python封装。
关于LTP更多的信息，欢迎访问LTP项目主页。

简介与背景知识
==============

pyltp是\ `语言技术平台(Language Technology Platform, LTP) <https://github.com/HIT-SCIR/ltp>`__\ 接口的一个Python封装。
本项目旨在使Python用户可以本地调用LTP。
该项目还处于测试状态，欢迎反馈bug。

在使用pyltp之前，您需要简要了解

* `什么是语言技术平台(LTP) <http://ltp.readthedocs.org/zh_CN/latest/index.html>`__\ ，它能否帮助您解决问题

一个简单的例子
=============

下面是使用pyltp进行分词的一个例子

::

    # -*- coding: utf-8 -*-
    from pyltp import Segmentor
    segmentor = Segmentor()
    segmentor.load("/path/to/your/cws/model")
    words = segmentor.segment("元芳你怎么看")
    print "|".join(words)
    segmentor.release()


除了分词之外，pyltp还提供词性标注、命名实体识别、依存句法分析、语义角色标注等功能。
更多例子，请参考示例代码\ `example/example.py <https://github.com/HIT-SCIR/pyltp/blob/master/example/example.py>`__\

安装
====

现阶段，pyltp主要在Linux编译测试。我们也欢迎用户提供其他平台的测试结果。

* 第一步，安装pyltp

使用pypi安装

::

    $ pip install pyltp

或从github源代码安装

::

    $ git clone https://github.com/HIT-SCIR/pyltp
    $ git submodule init
    $ git submodule update
    $ python setup.py build

* 第二步，下载模型文件

当前模型版本：3.3.0

下载地址\ `百度云 <http://pan.baidu.com/share/link?shareid=1988562907&uk=2738088569>`__\

版本对应
=====

* LTP版本: 3.3.0
* 模型版本: 3.3.0

作者
====

-  徐梓翔 << zxxu@ir.hit.edu.cn >> 2015-01-20 解决跨平台运行问题
-  刘一佳 << yjliu@ir.hit.edu.cn >> 2014-06-12 重组项目
-  HuangFJ << biohfj@gmail.com >> 本项目最初作者

.. |Pypi Status| image:: https://pypip.in/v/pyltp/badge.png
   :target: https://pypi.python.org/pypi/pyltp

.. |Build Status| image:: https://travis-ci.org/HIT-SCIR/pyltp.svg?branch=master
   :target: https://travis-ci.org/HIT-SCIR/pyltp
