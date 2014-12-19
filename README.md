pyltp<sup>beta</sup>: the python extension for LTP
----
[![Build Status](https://travis-ci.org/HIT-SCIR/pyltp.svg?branch=master)](https://travis-ci.org/HIT-SCIR/pyltp)

pyltp是[语言技术平台(Language Technology Platform, LTP)](https://github.com/HIT-SCIR/ltp)的Python封装。 关于LTP更多的信息，欢迎访问LTP项目主页。

### 作者

* 刘一佳 << yjliu@ir.hit.edu.cn >> 2014-06-12 重组项目
* HuangFJ << biohfj@gmail.com >> 本项目最初作者

# 简介与背景知识

pyltp是[语言技术平台(Language Technology Platform, LTP)](https://github.com/HIT-SCIR/ltp)接口的一个Python封装。
本项目旨在使Python用户可以本地调用LTP。
该项目还处于测试状态，欢迎反馈bug。

在使用pyltp之前，您需要简要了解
* [什么是语言技术平台](https://github.com/HIT-SCIR/ltp/blob/master/doc/ltp-document-3.0.md#%E7%AE%80%E4%BB%8B)，它能否帮助您解决问题
* [如何安装语言技术平台](https://github.com/HIT-SCIR/ltp/blob/master/doc/ltp-document-3.0.md#%E5%A6%82%E4%BD%95%E5%AE%89%E8%A3%85ltp)
* [语言技术平台提供哪些编程接口](https://github.com/HIT-SCIR/ltp/blob/master/doc/ltp-document-3.0.md#%E7%BC%96%E7%A8%8B%E6%8E%A5%E5%8F%A3)

如果您对这些问题不了解，请首先阅读我们提供的有关语言技术平台的文档。
在本文档的后续中，我们假定您已经阅读并成功编译并使用语言技术平台。

# 安装

## Unix编译

建议您使用github的开发版的pyltp，您可以采用如下命令编译pyltp

```
$ git clone https://github.com/HIT-SCIR/pyltp
$ git submodule init
$ git submodule update
$ python setup.py build
```

### Python开发版

在unix环境下编译时，请确保对应的python是dev版。您可以使用

* Ubuntu/Debian
```
$ [sudo] apt-get install python-dev
```
* Fedora
```
$ [sudo] yum install python-devel
```
安装dev版的python。

### Python3

pyltp主要采用python2.7开发。但经测试，其python3下也可以使用。
需要注意一点，请保证`python-config`与`python`命令指向相同的版本。

具体的检查方法可以用`python-config --includes`和`python --version`命令。

* python2.7环境下

```
$ python --version
Python 2.7.5+
$ python-config --includes
-I/usr/include/python2.7 ..
```

* python3环境下
```
$ python --version
Python 3.3.2+
$ python-config --includes
-I/usr/include/python3.3m ..
```

请确保编译环境与运行环境使用相同python版本。

## MSVC编译

尚处于测试阶段


# 例子

```
# -*- coding: utf-8 -*-
from pyltp import Segmentor
segmentor = Segmentor()
segmentor.load("/path/to/your/cws/model")
words = segmentor.segment("元芳你怎么看")
print "|".join(words)
```

# 文档

待完善
