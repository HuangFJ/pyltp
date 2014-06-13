#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
ROOTDIR = os.path.join(os.path.dirname(__file__), os.pardir)
sys.path.append(os.path.join(ROOTDIR, "lib"))

# Set your own model path
MODELDIR=os.path.join(ROOTDIR, "ltp_data")

from pyltp import Segmentor, Postagger, Parser, NamedEntityRecognizer, SementicRoleLabeller

sentence = "中国进出口银行与中国银行加强合作"

segmentor = Segmentor()
segmentor.load(os.path.join(MODELDIR, "cws.model"))
words = segmentor.segment(sentence)
print "\t".join(words)

postagger = Postagger()
postagger.load(os.path.join(MODELDIR, "pos.model"))
postags = postagger.postag(words)
print "\t".join(postags)

parser = Parser()
parser.load(os.path.join(MODELDIR, "parser.model"))
arcs = parser.parse(words, postags)

print "\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs)

recognizer = NamedEntityRecognizer()
recognizer.load(os.path.join(MODELDIR, "ner.model"))
netags = recognizer.recognize(words, postags)
print "\t".join(netags)

labeller = SementicRoleLabeller()
labeller.load(os.path.join(MODELDIR, "srl/"))
#labeller.load("/home/yjliu/ltp/model/srl/")
roles = labeller.label(words, postags, netags, arcs)

for role in roles:
    print role.index, "".join(
            ["%s:(%d,%d)" % (arg.name, arg.range.start, arg.range.end) for arg in role.arguments])
