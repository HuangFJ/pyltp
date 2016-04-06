===================================
pyltp: the python extension for LTP
===================================

|PyPI Status| |Build Status| |PyPI Downloads|

pyltp是\ `语言技术平台（Language Technology Platform, LTP）<https://github.com/HIT-SCIR/ltp>`__\ 的Python封装。

在使用pyltp之前，您需要简要了解：\ `什么是语言技术平台（LTP）<http://ltp.readthedocs.org/zh_CN/latest/index.html>`__\ ，它能否帮助您解决问题

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

* 第一步，安装pyltp

	使用pip安装

	::

    	$ pip install pyltp

	或从源代码安装

	::

    	$ git clone https://github.com/HIT-SCIR/pyltp
    	$ git submodule init
    	$ git submodule update
    	$ python setup.py install

* 第二步，下载模型文件

	下载地址\ `百度云 <http://pan.baidu.com/share/link?shareid=1988562907&uk=2738088569>`__\，当前模型版本：3.3.1

版本对应
========

* pyltp版本：0.1.9
* LTP版本：3.3.1
* 模型版本：3.3.1

作者
====

-  徐梓翔 << zxxu@ir.hit.edu.cn >> 2015-01-20 解决跨平台运行问题
-  刘一佳 << yjliu@ir.hit.edu.cn >> 2014-06-12 重组项目
-  HuangFJ << biohfj@gmail.com >> 本项目最初作者

.. |PyPI Status| image:: https://badge.fury.io/py/pyltp.svg
   :target: https://badge.fury.io/py/pyltp

.. |Build Status| image:: https://travis-ci.org/HIT-SCIR/pyltp.svg?branch=master
   :target: https://travis-ci.org/HIT-SCIR/pyltp

.. |PyPI Downloads| image:: https://img.shields.io/pypi/dm/pyltp.svg
   :target: https://pypi.python.org/pypi/pyltp
