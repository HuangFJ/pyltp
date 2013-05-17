#include <stdlib.h>
#include <boost/python.hpp>
#include "Xml4nlp.h"
#include "Ltp.h"


using namespace boost::python;


static XML4NLP xml4nlp;
static LTP ltp(xml4nlp);


struct PyLTP
{
public:
	PyLTP() {}

	boost::python::list ws(string mMsg){
		boost::python::list r;
		xml4nlp.CreateDOMFromString(mMsg);

		ltp.crfWordSeg();
		int wordNum = xml4nlp.CountWordInDocument();
		for (int i = 0; i < wordNum; ++i)
		{
			string word = xml4nlp.GetWord(i);
			if (! word.empty())
			{
				r.append(word);
			}
		}

		return r;
	}

	boost::python::list pos(string mMsg){
		boost::python::list r;
		xml4nlp.CreateDOMFromString(mMsg);

		ltp.postag();
		int wordNum = xml4nlp.CountWordInDocument();
		for (int i = 0; i < wordNum; ++i)
		{
			string word = xml4nlp.GetWord(i);
			string pos = xml4nlp.GetPOS(i);
			dict item;
			if (! word.empty())
			{
				item["cont"] = word;
				item["pos"] = pos;
				r.append(item);
			}
		}

		return r;
	}

	boost::python::list ner(string mMsg){
		boost::python::list r;
		xml4nlp.CreateDOMFromString(mMsg);

		ltp.ner();
		int wordNum = xml4nlp.CountWordInDocument();
		for (int i = 0; i < wordNum; ++i)
		{
			string word = xml4nlp.GetWord(i);
			string pos = xml4nlp.GetPOS(i);
			string ne = xml4nlp.GetNE(i);
			dict item;
			if (! word.empty())
			{
				item["cont"] = word;
				item["pos"] = pos;
				item["ne"] = ne;
				r.append(item);
			}
		}

		return r;
	}

	boost::python::list srl(string mMsg){
		boost::python::list r;
		xml4nlp.CreateDOMFromString(mMsg);

		ltp.srl();
		int wordNum = xml4nlp.CountWordInDocument();
		for (int i = 0; i < wordNum; ++i)
		{
			string word = xml4nlp.GetWord(i);
			string pos = xml4nlp.GetPOS(i);
			string ne = xml4nlp.GetNE(i);

			pair<int, const char *> parent_relate;
			xml4nlp.GetParse(parent_relate,i);

			boost::python::list args;
			int argNum = xml4nlp.CountPredArgToWord(i);
			if (argNum > 0)
			{
				vector<const char *> vecType(argNum);
				vector< pair<int, int> > vecBegEnd(argNum);
				xml4nlp.GetPredArgToWord(i,vecType,vecBegEnd);

				for(int j = 0; j < argNum; ++j){
					dict arg;
					arg["type"] = vecType[j];
					arg["beg"] = (vecBegEnd[j]).first;
					arg["end"] = (vecBegEnd[j]).second;

					args.append(arg);
				}

			}

			dict item;
			if (! word.empty())
			{
				item["cont"] = word;
				item["pos"] = pos;
				item["ne"] = ne;
				item["parent"] = parent_relate.first;
				item["relate"] = parent_relate.second;
				item["args"] = args;
				r.append(item);
			}
		}

		return r;
	}
};

BOOST_PYTHON_MODULE(pyltp)
{
	class_<PyLTP>("LTP")
			.def("ws", &PyLTP::ws)
			.def("pos", &PyLTP::pos)
			.def("ner", &PyLTP::ner)
			.def("srl", &PyLTP::srl)
	;
}
