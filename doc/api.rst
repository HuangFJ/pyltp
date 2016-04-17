使用 pyltp
===========
pyltp 是 `LTP <https://github.com/HIT-SCIR/ltp>`_ 的 Python 封装，提供了分词，词性标注，命名实体识别，依存句法分析，语义角色标注的功能。

关于各个模块任务的介绍、标注体系、性能指标，可以查阅 `这里 <http://www.ltp-cloud.com/intro/#introduction>`_ 的介绍。

编码
-----

pyltp 的所有输入的分析文本和输出的结果的编码均为 UTF-8。

由于 Windows 终端采用 GBK 编码显示，直接输出 pyltp 的分析结果会在终端显示为乱码。您可以将标准输出重定向到文件，以 UTF8 方式查看文件，就可以解决显示乱码的问题。


分句
-----


分词
-----

使用 pyltp 进行分词示例如下 ::

    # -*- coding: utf-8 -*-
    from pyltp import Segmentor
    segmentor = Segmentor()  # 初始化实例
    segmentor.load('/path/to/your/model')  # 加载模型
    words = segmentor.segment('元芳你怎么看')  # 分词
    print '|'.join(words)
    segmentor.release()  # 释放模型
    
:file:`/path/to/your/model` 请替换成 LTP 分词模型文件路径，默认模型文件名为 :file:`cws.model` 。

:code:`words = segmentor.segment(u'元芳你怎么看')` 的返回值类型是

使用分词外部词典
~~~~~~~~~~~~~~~~

pyltp 分词支持用户使用自定义词典。分词外部词典本身是一个文本文件（plain text），每行指定一个词，编码同样须为 UTF-8，样例如下所示 ::

    苯并芘
    亚硝酸盐

示例如下 ::

    # -*- coding: utf-8 -*-
    from pyltp import Segmentor
    segmentor = Segmentor()  # 初始化实例
    segmentor.load_with_lexicon('/path/to/your/model', '/path/to/your/lexicon') # 加载模型
    words = segmentor.segment('亚硝酸盐是一种化学物质')
    print '\t'.join(words)
    segmentor.release()


使用个性化分词模型
~~~~~~~~~~~~~~~~~~~

个性化分词是 LTP 的特色功能。个性化分词为了解决测试数据切换到如小说、财经等不同于新闻领域的领域。 在切换到新领域时，用户只需要标注少量数据。 个性化分词会在原有新闻数据基础之上进行增量训练。 从而达到即利用新闻领域的丰富数据，又兼顾目标领域特殊性的目的。

pyltp 支持使用用户训练好的个性化模型。关于个性化模型的训练需使用 LTP，详细介绍和训练方法请参考 `个性化分词 <http://ltp.readthedocs.org/zh_CN/latest/theory.html#customized-cws-reference-label>`_。

在 pyltp 中使用个性化分词模型的示例如下 ::

    # -*- coding: utf-8 -*-
    from pyltp import CustomizedSegmentor
    customized_segmentor = CustomizedSegmentor()  # 初始化实例
    customized_segmentor.load('/path/to/your/base_model', '/path/to/your/customized_model') # 加载模型
    words = customized_segmentor.segment('亚硝酸盐是一种化学物质')
    print '\t'.join(words)
    customized_segmentor.release()

同样，使用个性化分词模型的同时也可以使用外部词典 ::

    # -*- coding: utf-8 -*-
    from pyltp import CustomizedSegmentor
    customized_segmentor = CustomizedSegmentor()  # 初始化实例
    customized_segmentor.load_with_lexicon('/path/to/your/base_model', '/path/to/your/customized_model', '/path/to/your/lexicon') # 加载模型
    words = customized_segmentor.segment('亚硝酸盐是一种化学物质')
    print '\t'.join(words)
    customized_segmentor.release()


词性标注
--------

使用 pyltp 进行词性标注示例如下 ::

    # -*- coding: utf-8 -*-
    from pyltp import Postagger
    postagger = Postagger() # 初始化实例
    postagger.load('/path/to/your/model')  # 加载模型
    postags = postagger.postag(words)  # 词性标注
    print '\t'.join(postags)
    postag.release()  # 释放模型
    
参数 :code:`words` 支持是列表，例如

    words = ['元芳', '你', '怎么', '看']

LTP 使用 863 词性标注集，详细请参考 `词性标注集 <http://ltp.readthedocs.org/zh_CN/latest/appendix.html#id3>`_。
    
使用词性标注外部词典
~~~~~~~~~~~~~~~~~~

pyltp 词性标注同样支持用户的外部词典。词性标注外部词典同样为一个文本文件，每行指定一个词，第一列指定单词，第二列之后指定该词的候选词性（可以有多项，每一项占一列），列与列之间用空格区分。示例如下 ::

    雷人 v a
    】 wp

命名实体识别
-----------

使用 pyltp 进行命名实体识别示例如下 ::

    # -*- coding: utf-8 -*-
    from pyltp import NamedEntityRecognizer
    recognizer = NamedEntityRecognizer() # 初始化实例
    recognizer.load('/path/to/your/model')  # 加载模型
    netags = recognizer.recognize(words, postags)  # 命名实体识别
    print '\t'.join(netags)
    recognizer.release()  # 释放模型

其中，:code:`words`和:code:`postags`分别为分词和词性标注的结果。


LTP 提供的命名实体类型为:人名、地名、机构名，详细请参考 `命名实体识别标注集 <http://ltp.readthedocs.org/zh_CN/latest/appendix.html#id4>`_。

依存句法分析
-----------

使用 pyltp 进行依存句法分析示例如下 ::

    # -*- coding: utf-8 -*-
    from pyltp import Parser
    parser = Parser() # 初始化实例
    parser.load('/path/to/your/model')  # 加载模型
    arcs = parser.parse(words, postags)  # 句法分析
    print "\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs)
    parser.release()  # 释放模型

其中，:code:`words`和:code:`postags`分别为分词和词性标注的结果。

标注集请参考 `依存句法关系 <http://ltp.readthedocs.org/zh_CN/latest/appendix.html#id5>`_。

语义角色标注
-----------

使用 pyltp 进行语义角色标注示例如下 ::

    # -*- coding: utf-8 -*-
    from pyltp import SementicRoleLabeller
    labeller = SementicRoleLabeller() # 初始化实例
    labeller.load('/path/to/your/model/dir')  # 加载模型
    roles = labeller.label(words, postags, netags, arcs)  # 语义角色标注
    for role in roles:
        print role.index, "".join(
            ["%s:(%d,%d)" % (arg.name, arg.range.start, arg.range.end) for arg in role.arguments])
    labeller.release()  # 释放模型


标注集请参考 `语义角色关系 <http://ltp.readthedocs.org/zh_CN/latest/appendix.html#id6>`_。

语义依存分析
-----------

pyltp 暂不提供语义依存分析功能。若需使用该功能，请使用 `语言云 <http://www.ltp-cloud.com>`_。


完整示例代码
-----------

完整的示例代码可以参考 :file:`example/example.py`。
