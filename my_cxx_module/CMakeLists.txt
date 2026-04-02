cmake_minimum_required(VERSION 3.18...4.0)
project(pybind11-project VERSION 0.7.5)

set(PY_VERSION_SUFFIX "")
set(PY_FULL_VERSION ${PROJECT_VERSION}${PY_VERSION_SUFFIX})

# Make sure that the Python and CMake versions match
if (DEFINED PY_BUILD_CMAKE_PROJECT_VERSION)
    if (NOT "${PY_BUILD_CMAKE_PROJECT_VERSION}" MATCHES "^${PY_FULL_VERSION}$")
        message(FATAL_ERROR "Version number does not match (${PY_BUILD_CMAKE_PROJECT_VERSION} - ${PY_FULL_VERSION}).")
    endif()
endif()

# Find the Python interpreter and the development files
find_package(Python3 REQUIRED COMPONENTS Interpreter Development.Module)

include(FetchContent)
FetchContent_Declare(
    pybind11
    URL https://github.com/pybind/pybind11/archive/refs/tags/v3.0.3.tar.gz
    URL_HASH MD5=e7f74c566e75924d02482333666a87d6
)
FetchContent_MakeAvailable(pybind11)

# Compile the example Python module
pybind11_add_module(module MODULE "src/native/module.cpp")
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
