/**
 * @file    Example C++ extension for Python using Pybind11 that adds two
 *          integers.
 */

#include <pybind11/pybind11.h>
#include <pybind11/pytypes.h>
#include <pybind11/stl.h>

#include <vector>
#include <cstdint>
#include <iostream>

void say(const std::string& s) {
    std::cout << s << std::endl;
}

void handle_bytes(const pybind11::bytes bytes) {
    std::string_view view = static_cast<std::string_view>(bytes);
    std::cout << "handle bytes [" << view.size() << "]" << std::endl;
}

void handle_bytearray(const pybind11::bytearray bytes) {
    std::cout << "handle bytearray [" << bytes.size() << "]" << std::endl;
}

std::string sum_as_string(int64_t a, int64_t b) {
    return std::to_string(a + b);
}

std::string greet(const std::string& name) {
    std::string greeting = "Hello, " + name + "!";
    return greeting;
}

PYBIND11_MODULE(MODULE_NAME, m) {
    m.doc()               = "Module for string operations.";
    m.attr("__version__") = VERSION_INFO;

    m.def("say",
          say,
	  "Say input string"
    );

    m.def("handle_bytes",
          handle_bytes,
	  "Method with a bytes input"
    );

    m.def("handle_bytearray",
          handle_bytearray,
	  "Method with a bytearray input"
    );

    m.def("sum_as_string",
	  sum_as_string,
	  "Sum two integers and return string"
    );

    m.def("greet",
        greet,
        "Say hello"
    );
}
