pyltp
----

<a href="https://github.com/HIT-SCIR/ltp">LTP</a> wrapper module for Python.

依赖
----

- python2.7
- gfortran （可选）

编译
----

```
$ git clone --recursive https://github.com/HuangFJ/pyltp
$ cd pyltp
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
