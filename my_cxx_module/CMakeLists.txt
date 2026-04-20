cmake_minimum_required(VERSION 3.18...4.0)
project(my_cxx_module VERSION 0.7.5)

set(PY_VERSION_SUFFIX "")
set(PY_FULL_VERSION ${PROJECT_VERSION}${PY_VERSION_SUFFIX})

# Make sure that the Python and CMake versions match
if (DEFINED PY_BUILD_CMAKE_PROJECT_VERSION)
    if (NOT "${PY_BUILD_CMAKE_PROJECT_VERSION}" MATCHES "^${PY_FULL_VERSION}$")
        message(FATAL_ERROR "Version number does not match (${PY_BUILD_CMAKE_PROJECT_VERSION} - ${PY_FULL_VERSION}).")
    endif()
endif()

# Find the Python development files
find_package(Python3 REQUIRED COMPONENTS Development.Module)

include(FetchContent)

FetchContent_Declare(
    pybind11
    URL https://github.com/pybind/pybind11/archive/refs/tags/v3.0.4.tar.gz
    URL_HASH MD5=933fa1b6b1fe34c9945ecb3fe67f5c4b
)
FetchContent_MakeAvailable(pybind11)

# Compile the example Python module
pybind11_add_module(module MODULE "src/native/module.cpp")
target_compile_definitions(module PRIVATE PYBIND11_HAS_STRING_VIEW)
set_target_properties(module PROPERTIES DEBUG_POSTFIX "${CMAKE_DEBUG_POSTFIX}${PYTHON_MODULE_DEBUG_POSTFIX}")
target_compile_definitions(module PRIVATE MODULE_NAME=$<TARGET_FILE_BASE_NAME:module> VERSION_INFO="${PY_FULL_VERSION}")

# Hide all symbols by default (including external libraries on Linux)
set_target_properties(module PROPERTIES CXX_VISIBILITY_PRESET "hidden" VISIBILITY_INLINES_HIDDEN true)
if (CMAKE_SYSTEM_NAME MATCHES "Linux")
    target_link_options(module PRIVATE "LINKER:--exclude-libs,ALL")
endif()

# Install the Python module
if (PY_BUILD_CMAKE_IMPORT_NAME)
    install(TARGETS module EXCLUDE_FROM_ALL COMPONENT python_modules DESTINATION ${PY_BUILD_CMAKE_IMPORT_NAME})
endif (PY_BUILD_CMAKE_IMPORT_NAME)
