cmake_minimum_required (VERSION 2.8.0)
project ("pyltp - LTP wrapper module for Python")

if (CMAKE_SYSTEM_PROCESSOR STREQUAL "x86_64")
    set (CMAKE_CXX_FLAGS ${CMAKE_CSS_FLAGS} "-fPIC")
endif (CMAKE_SYSTEM_PROCESSOR STREQUAL "x86_64")

# project attributes section
#set (LTP_MODULE_PATH        ${PROJECT_SOURCE_DIR}/ltp)
set (LTP_HOME  ${PROJECT_SOURCE_DIR}/ltp)

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

#execute_process (COMMAND 
#    python -c "from distutils import sysconfig; print sysconfig.get_config_var('LIBDIR')"
#    OUTPUT_VARIABLE PYTHON_LIBRARY_DIR)

#execute_process (COMMAND 
#    python -c "from distutils import sysconfig; print sysconfig.get_config_var('INCLUDEDIR')"
#    OUTPUT_VARIABLE PYTHON_INCLUDE_DIR)

#message (STATUS ${PYTHON_INCLUDE_DIR})
#message (STATUS ${PYTHON_LIBRARY_DIR})

# -- config python directories

# -- config boost directories
set (BOOST_INCLUDE_DIR     /usr/include/boost)

# compiling section
# -- compile shipped libraries
# add_subdirectory (ltp/thirdparty)

# -- compile source code
# add_subdirectory (ltp/src)

# compile pyltp
# add_subdirectory (boost_python)

add_subdirectory (src)
