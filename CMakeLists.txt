cmake_minimum_required (VERSION 2.8.0)
project ("pyltp - LTP wrapper module for Python")

if (CMAKE_SYSTEM_PROCESSOR STREQUAL "x86_64")
    set (CMAKE_CXX_FLAGS ${CMAKE_CSS_FLAGS} "-fPIC")
endif (CMAKE_SYSTEM_PROCESSOR STREQUAL "x86_64")

# project attributes section
set (LTP_MODULE_PATH        ${PROJECT_SOURCE_DIR}/ltp)

# -- config cmake modules path
set (CMAKE_MODULE_PATH      ${LTP_MODULE_PATH}/cmake)

# -- config output directories
set (LIBRARY_OUTPUT_PATH    ${PROJECT_SOURCE_DIR}/lib)
set (INCLUDE_OUTPUT_PATH    ${PROJECT_SOURCE_DIR}/include)

# -- config LTP directories
set (SOURCE_DIR             ${LTP_MODULE_PATH}/src)
set (THIRDPARTY_DIR         ${LTP_MODULE_PATH}/thirdparty)
set (TOOLS_DIR              ${LTP_MODULE_PATH}/tools)
set (CONFIGURE_DIR          ${LTP_MODULE_PATH}/conf)
set (MODEL_DIR              ${LTP_MODULE_PATH}/ltp_data)
set (DATA_DIR               ${LTP_MODULE_PATH}/test_data)

# -- config python directories
set (PYTHON_INCLUDE_DIR     /usr/include/python2.7)
set (PYTHON_LIBRARY_PATH    /usr/lib/libpython2.7.a)

# -- config boost directories
set (BOOST_INCLUDE_DIR     /usr/include/boost)

# compiling section
# -- compile shipped libraries
add_subdirectory (ltp/thirdparty)

# -- compile source code
add_subdirectory (ltp/src)

# -- generate configure file for pyltp.so
configure_file (
    ${CONFIGURE_DIR}/ltp_all_modules.conf.in
    ${LIBRARY_OUTPUT_PATH}/ltp_all_modules.conf)

# compile pyltp
add_subdirectory (src)
add_subdirectory (boost_python)
