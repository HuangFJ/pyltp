# -*- coding: utf-8 -*-
#!/usr/bin/env python

# add project root lib into sys.path
import sys, os
ROOTDIR = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.append(os.path.join(ROOTDIR, "lib"))

from pyltp import LTP

ltp = LTP("./ltp.cnf")

print ltp.ws(u'元芳你怎么看？'.encode('utf8'))
print ltp.pos(u'元芳你怎么看？'.encode('utf8'))
print ltp.ner(u'元芳你怎么看？'.encode('utf8'))
print ltp.srl(u'元芳你怎么看？'.encode('utf8'))
