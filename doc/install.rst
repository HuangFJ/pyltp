安装 pyltp
===========

* 注：由于新版本增加了新的第三方依赖如dynet等，不再支持 windows 下 python2 环境。

使用 pip 安装
-------------

使用 pip 安装前，请确保您已安装了 `pip <https://pip.pypa.io/>`_ ::

    $ pip install pyltp

接下来，需要下载 LTP 模型文件。

* 下载地址 - `模型下载 http://ltp.ai/download.html`_
* 当前模型版本 - 3.4.0
* 注意在windows下 3.4.0 版本的 语义角色标注模块 模型需要单独下载，具体查看下载地址链接中的说明。

请确保下载的模型版本与当前版本的 pyltp 对应，否则会导致程序无法正确加载模型。

从源码安装
---------

您也可以选择从源代码编译安装 ::

    $ git clone https://github.com/HIT-SCIR/pyltp
    $ git submodule init
    $ git submodule update
    $ python setup.py install

安装完毕后，也需要下载相应版本的 LTP 模型文件。
