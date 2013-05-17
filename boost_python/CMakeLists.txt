include_directories (${BOOST_INCLUDE_DIR}
    ${PYTHON_INCLUDE_DIR})

add_library (boost_python
    src/converter/arg_to_python_base.cpp
    src/converter/from_python.cpp
    src/converter/type_id.cpp
    src/converter/builtin_converters.cpp
    src/converter/registry.cpp
    src/object/class.cpp
    src/object/function_doc_signature.cpp
    src/object/life_support.cpp
    src/object/enum.cpp
    src/object/inheritance.cpp
    src/object/pickle_support.cpp
    src/object/function.cpp
    src/object/iterator.cpp
    src/object/stl_iterator.cpp
    src/import.cpp
    src/numeric.cpp
    src/slice.cpp
    src/dict.cpp
    src/list.cpp
    src/str.cpp
    src/errors.cpp
    src/long.cpp
    src/object_operators.cpp
    src/tuple.cpp
    src/exec.cpp
    src/module.cpp
    src/object_protocol.cpp
    src/wrapper.cpp)
