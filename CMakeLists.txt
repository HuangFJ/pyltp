cmake_minimum_required (VERSION 2.8.0)
project ("pyltp - LTP wrapper module for Python")

if (CMAKE_SYSTEM_PROCESSOR STREQUAL "x86_64")
    set (CMAKE_CXX_FLAGS ${CMAKE_CSS_FLAGS} "-fPIC")
endif (CMAKE_SYSTEM_PROCESSOR STREQUAL "x86_64")

# project attributes section
set (LTP_HOME "/path/to/your/ltp/" CACHE STRING "Use to specified ltp path")

# -- config cmake modules path
set (CMAKE_MODULE_PATH      ${LTP_MODULE_PATH}/cmake)

# -- config output directories
set (LIBRARY_OUTPUT_PATH    ${PROJECT_SOURCE_DIR}/lib)
set (INCLUDE_OUTPUT_PATH    ${PROJECT_SOURCE_DIR}/include)

# -- config boost directories
set (BOOST_INCLUDE_DIR ${PROJECT_SOURCE_DIR}/boost_python/include)

# compiling section
# -- compile shipped libraries
# add_subdirectory (ltp/thirdparty)

# -- compile source code
# add_subdirectory (ltp/src)

# compile pyltp
add_subdirectory (boost_python)

add_subdirectory (src)
