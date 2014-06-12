/**
 * pyltp - A python extension for Language Technology Platform
 *
 *  @author: HuangFJ
 *  @author: LIU, Yijia <yjliu@ir.hit.edu.cn>
 */
#include <iostream>
#include <vector>
#include <boost/python.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>
#include "ltp/segment_dll.h"
// #include "ltp/postagger_dll.h"
// #include "ltp/parser_dll.h"
// #include "ltp/ner_dll.h"
// #include "ltp/SRL_dll.h"


struct Segmentor {
  Segmentor()
    : model(NULL) {}

  void load(std::string model_path) {
    if (model == NULL) {
      model = segmentor_create_segmentor(model_path.c_str());
    } else {
      std::cerr << "Model reloaded!" << std::endl;
    }
  }

  void load_with_lexicon(std::string model_path, std::string lexicon_path) {
    if (model == NULL) {
      model = segmentor_create_segmentor(model_path.c_str(), lexicon_path.c_str());
    } else {
      std::cerr << "Model reloaded!" << std::endl;
    }
  }

  std::vector<std::string> segment(std::string sentence) {
    std::vector<std::string> ret;
    segmentor_segment(model, sentence.c_str(), ret);
    return ret;
  }

  void release() {
    segmentor_release_segmentor(model);
  }

  void * model;
};


BOOST_PYTHON_MODULE(pyltp)
{
  using namespace boost::python;

  class_< std::vector<std::string> >("VectorOfString")
    .def(vector_indexing_suite< std::vector<std::string> >() )
    ;

  class_<Segmentor>("Segmentor")
    .def("load", &Segmentor::load)
    .def("load_with_lexicon", &Segmentor::load_with_lexicon)
    .def("segment", &Segmentor::segment)
    .def("release", &Segmentor::release)
    ;
}
