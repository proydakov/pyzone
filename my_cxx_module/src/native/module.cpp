/**
 * @file    Example C++ extension for Python using Pybind11 that adds two
 *          integers.
 */

#include <cstdint>
#include <pybind11/pybind11.h>

using pybind11::operator""_a;

std::string sum_as_string(int64_t a, int64_t b) {
    return std::to_string(a + b);
}

std::string greet(const std::string& name) {
    std::string greeting = "Hello, " + name + "!";
    return greeting;
}

PYBIND11_MODULE(MODULE_NAME, m) {
    m.doc()               = "Module for adding integers";
    m.attr("__version__") = VERSION_INFO;

    m.def("sum_as_string",
	  sum_as_string,
	  "a"_a, "b"_a,
	  "Sum two integers and return string"
    );

    m.def("greet",
        greet,
        "name"_a,
        "Say hello"
    );
}
