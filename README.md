pyltp
----

<a href="https://github.com/HIT-SCIR/ltp">LTP</a> 的 Python 封装。

依赖
----

- python
- cmake 2.8
- boost 1.53
- gfortran （可选）

编译
----

```
$ git clone --recursive https://github.com/HuangFJ/pyltp
$ cd pyltp
```
编辑CMakeLists.txt，配置boost和python参数

```
# -- config python directories
set (PYTHON_INCLUDE_DIR     /usr/local/python-2.7/include/python2.7)
set (PYTHON_LIBRARY_PATH    /usr/local/python-2.7/lib/libpython2.7.a)

# -- config boost directories
set (BOOST_INCLUDE_DIR     /usr/local/boost_1_53_0/)
```

```
$ ./configure
$ make
```

编译成功之后会在lib目录下生成pyltp.so和ltp_all_modules.conf文件。在ltp_all_modules.conf里面配置<a href="http://ir.hit.edu.cn/ltp/program/ltp_data.zip">ltp_data</a>文件夹的路径。

使用
----

```
$ cd lib
$ python
```
```
>>> from pyltp import LTP
>>> ltp = LTP()
>>> ltp.ws(u'元芳你怎么看？'.encode('gbk'))
>>> ltp.pos(u'元芳你怎么看？'.encode('gbk'))
>>> ltp.ner(u'元芳你怎么看？'.encode('gbk'))
>>> ltp.srl(u'元芳你怎么看？'.encode('gbk'))
```

应注意获得的结果是gbk编码，所以要在你的代码中还要把gbk再转回utf－8
