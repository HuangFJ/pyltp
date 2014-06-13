#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
ROOTDIR = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.append(os.path.join(ROOTDIR, "lib"))

from pyltp import Segmentor, Postagger, Parser, NamedEntityRecognizer, SementicRoleLabeller

segmentor = Segmentor()
segmentor.load("/home/yjliu/ltp/model/cws.model")
words = segmentor.segment("元芳你怎么看")
print "|".join(words)

postagger = Postagger()
postagger.load("/home/yjliu/ltp/model/pos.model")
postags = postagger.postag(words)
print "|".join(postags)

parser = Parser()
parser.load("/home/yjliu/ltp/model/parser.model")
arcs = parser.parse(words, postags)

for arc in arcs:
    print arc.head, arc.relation

recognizer = NamedEntityRecognizer()
recognizer.load("/home/yjliu/ltp/model/ner.model")
netags = recognizer.recognize(words, postags)
print "|".join(netags)

labeller = SementicRoleLabeller()
labeller.load("/home/yjliu/ltp/model/SRL/")
roles = labeller.label(words, postags, netags, arcs)
for role in roles:
    print role
