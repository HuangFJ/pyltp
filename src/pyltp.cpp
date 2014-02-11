#include <stdlib.h>
#include <boost/python.hpp>
#include "Xml4nlp.h"
#include "Ltp.h"

using namespace boost::python;

struct PyLTP
{
  private:
    XML4NLP xml4nlp;
    LTP ltp;

  public:
    PyLTP(): ltp() {}
    PyLTP(string config_file): ltp(config_file.c_str()) {}

    string ws(string mMsg){
      xml4nlp.CreateDOMFromString(mMsg);

      ltp.wordseg(xml4nlp);
      string result;
      xml4nlp.SaveDOM(result);
      xml4nlp.ClearDOM();

      return result;
    }

    string pos(string mMsg){
      xml4nlp.CreateDOMFromString(mMsg);

      ltp.postag(xml4nlp);
      string result;
      xml4nlp.SaveDOM(result);
      xml4nlp.ClearDOM();

      return result;
    }

    string ner(string mMsg){
      xml4nlp.CreateDOMFromString(mMsg);

      ltp.ner(xml4nlp);
      string result;
      xml4nlp.SaveDOM(result);
      xml4nlp.ClearDOM();

      return result;
    }

    string dp(string mMsg){
      xml4nlp.CreateDOMFromString(mMsg);

      ltp.parser(xml4nlp);
      string result;
      xml4nlp.SaveDOM(result);
      xml4nlp.ClearDOM();

      return result;
    }

    string srl(string mMsg){
      xml4nlp.CreateDOMFromString(mMsg);

      ltp.srl(xml4nlp);
      string result;
      xml4nlp.SaveDOM(result);
      xml4nlp.ClearDOM();

      return result;
    }
};

BOOST_PYTHON_MODULE(pyltp)
{
  class_<PyLTP>("LTP", init<string>())
    .def(init<>())
    .def("ws", &PyLTP::ws)
    .def("pos", &PyLTP::pos)
    .def("ner", &PyLTP::ner)
    .def("dp", &PyLTP::dp)
    .def("srl", &PyLTP::srl)
    ;
}
