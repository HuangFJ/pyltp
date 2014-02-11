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

编译成功之后会在lib目录下生成pyltp.so。使用时，需要将`{PROJECT_PATH}/lib`加入python的sys.path中。`example/example.py`显示了具体做法。

使用
----

```
$ cd lib
$ python
```
```
>>> from pyltp import LTP
>>> ltp = LTP("./ltp.conf")
>>> ltp.ws(u'元芳你怎么看？'.encode('utf8'))
>>> ltp.pos(u'元芳你怎么看？'.encode('utf8'))
>>> ltp.ner(u'元芳你怎么看？'.encode('utf8'))
>>> ltp.srl(u'元芳你怎么看？'.encode('utf8'))
```

应注意获得的结果是xml形式，并以utf8编码。
