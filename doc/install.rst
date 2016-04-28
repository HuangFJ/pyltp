安装 pyltp
===========

使用 pip 安装
-------------

使用 pip 安装前，请确保您已安装了 `pip <https://pip.pypa.io/>`_ ::

    $ pip install pyltp

接下来，需要下载 LTP 模型文件。

* 下载地址 - `百度云 <http://pan.baidu.com/share/link?shareid=1988562907&uk=2738088569>`_
* 当前模型版本 - 3.3.1

请确保下载的模型版本与当前版本的 pyltp 对应，否则会导致程序无法正确加载模型。

从源码安装
---------

您也可以选择从源代码编译安装 ::

    $ git clone https://github.com/HIT-SCIR/pyltp
    $ git submodule init
    $ git submodule update
    $ python setup.py install

安装完毕后，也需要下载相应版本的 LTP 模型文件。
