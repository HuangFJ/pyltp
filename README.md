# pyltp

[![PyPI Status](https://badge.fury.io/py/pyltp.svg)](https://badge.fury.io/py/pyltp)
[![Build Status](https://travis-ci.org/HIT-SCIR/pyltp.svg?branch=master)](https://travis-ci.org/HIT-SCIR/pyltp)
[![PyPI Downloads](https://img.shields.io/pypi/dm/pyltp.svg)](https://pypi.python.org/pypi/pyltp)

pyltp是 [语言技术平台（Language Technology Platform, LTP）](https://github.com/HIT-SCIR/ltp) 的Python封装。

在使用pyltp之前，您需要简要了解 [语言技术平台（LTP）](http://ltp.readthedocs.org/zh_CN/latest/) 能否帮助您解决问题。

## 一个简单的例子

下面是一个使用pyltp进行分词的例子

```python
# -*- coding: utf-8 -*-
from pyltp import Segmentor
segmentor = Segmentor()
segmentor.load("/path/to/your/cws/model")
words = segmentor.segment("元芳你怎么看")
print "|".join(words)
segmentor.release()
```
除了分词之外，pyltp还提供词性标注、命名实体识别、依存句法分析、语义角色标注等功能。

详细使用方法请参考 [在线文档](http://ltp-pyltp.readthedocs.org/)。

## 安装

* 第一步，安装pyltp

	使用pip安装

	```
	$ pip install pyltp
	```
	或从源代码安装
	
	```
	$ git clone https://github.com/HIT-SCIR/pyltp
	$ git submodule init
	$ git submodule update
	$ python setup.py install
	```

* 第二步，下载模型文件

	[百度云](http://pan.baidu.com/share/link?shareid=1988562907&uk=2738088569)，当前模型版本3.3.1

## 版本对应

* pyltp 版本：0.1.9
* LTP 版本：3.3.1
* 模型版本：3.3.1

## 作者

* 徐梓翔 << zxxu@ir.hit.edu.cn >> 2015-01-20 解决跨平台运行问题
* 刘一佳 << yjliu@ir.hit.edu.cn >> 2014-06-12 重组项目
* HuangFJ << biohfj@gmail.com >> 本项目最初作者
