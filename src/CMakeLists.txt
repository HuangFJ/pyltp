find_package(PythonLibs REQUIRED)

include_directories (
    ${BOOST_INCLUDE_DIR}
    ${PYTHON_INCLUDE_DIRS}
    ${LTP_HOME}/include)

set (pyltp_SRC  pyltp.cpp)

link_directories (
    ${LTP_HOME}/lib)

add_library (pyltp SHARED ${pyltp_SRC})
set_target_properties (pyltp PROPERTIES PREFIX "")

target_link_libraries (pyltp
    segmentor
    postagger
    parser
    ner
    srl
    boost_python_shared_lib
    ${PYTHON_LIBRARIES})

