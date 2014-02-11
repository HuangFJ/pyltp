include_directories (${BOOST_INCLUDE_DIR}
    ${PYTHON_INCLUDE_DIR})

include_directories (./
    ${SOURCE_DIR}/__util
    ${SOURCE_DIR}/__xml4nlp
    ${SOURCE_DIR}/_split_sentence
    ${SOURCE_DIR}/_ner
    ${SOURCE_DIR}/_srl
    ${SOURCE_DIR}/__ltp_dll
    ${THIRDPARTY_DIR}/crfpp
    ${THIRDPARTY_DIR}/maxent
    ${THIRDPARTY_DIR}/tinyxml)

set (pyltp_SRC	pyltp.cpp)

link_directories (${LIBRARY_OUTPUT_PATH})

add_library (pyltp SHARED ${pyltp_SRC})
set_target_properties (pyltp PROPERTIES PREFIX "")

target_link_libraries (pyltp
    maxent_static_lib
    util_static_lib
    ltp
    splitsnt
    segmentor_static_lib
    postagger_static_lib
    parser_static_lib
    ner_static_lib
    srl_static_lib
    xml4nlp
    boost_regex_static_lib
    boost_python_static_lib
    dl
    pthread
    ${PYTHON_LIBRARY_PATH})
