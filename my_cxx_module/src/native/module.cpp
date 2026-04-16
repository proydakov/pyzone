/**
 * @file    Example C++ extension for Python using Pybind11
 */

#include <pybind11/pybind11.h>
#include <pybind11/pytypes.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>

#include <string>
#include <vector>
#include <cstdint>
#include <iostream>

class ISpeech
{
public:
    ISpeech(std::string iname) : name(std::move(iname))
    {
    }

    virtual ~ISpeech() = default;
    virtual void Talk() = 0;

    std::string name;
};

class SpeechV1 final : public ISpeech
{
public:
    SpeechV1(std::string iname) : ISpeech(std::move(iname))
    {
    }

    void Talk() override
    {
        std::cout << "Talking [" << name << "] with Speech version 1.0. \n";
    }
};

class SpeechV2 final : public ISpeech
{
public:
    SpeechV2(std::string iname) : ISpeech(std::move(iname))
    {
    }

    void Talk() override
    {
        std::cout << "Talking [" << name << "] with Speech version 2.0. \n";
    }
};

class IRobot
{
public:
    std::string name;
    ISpeech &speech;

    IRobot(std::string iname, ISpeech &ispeech) :
        name(std::move(iname)),
        speech(ispeech)
    {
    }

    virtual ~IRobot() = default;

    virtual void Walk() = 0;
    void Talk() { speech.Talk(); }
};

class T800 final : public IRobot
{
public:
    int year;

    T800(std::string name, int year_, ISpeech &speech_)
        : IRobot(std::move(name), speech_), year(year_)
    {
    }

    virtual void Walk() override
    {
        std::cout << "T-800 is walking...\n";
    };
};

class T1000 final : public IRobot
{
    double height;

public:
    T1000(std::string name, double height_, ISpeech &speech_)
        : IRobot(std::move(name), speech_), height(height_)
    {
    }

    double GetHeight()
    {
        return height;
    }

    auto SetHeight(double height_)
    {
        height = height_;
    }

    virtual void Walk() override
    {
        std::cout << "T-1000 is walking...\n";
    };

    auto GetData()
    {
        std::vector<std::tuple<std::string, double>> data;
        data.push_back(std::make_tuple("book", 1.5));
        data.push_back(std::make_tuple("table", 2.5));
        data.push_back(std::make_tuple("wall", 3.5));
        return data;
    }
};

void Move(IRobot& robot){
    std::cout<< robot.name << " ";
    robot.Walk();
}

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

void handle_list_num(const std::vector<int64_t>& list) {
    std::cout << "list(i64)[" << list.size() << "]";
    for(auto const e : list) {
        std::cout << " " << e;
    }
    std::cout << std::endl;
}

void handle_list_real(const std::vector<double>& list) {
    std::cout << "list(f64)[" << list.size() << "]";
    for(auto const e : list) {
        std::cout << " " << e;
    }
    std::cout << std::endl;
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

    m.def("handle_list_num",
        handle_list_num,
        "Method with a list of integers input"
    );

    m.def("handle_list_real",
        handle_list_real,
        "Method with a list of reals input"
    );

    m.def("sum_as_string",
	    sum_as_string,
        "Sum two integers and return string"
    );

    m.def("greet",
        greet,
        "Say hello"
    );

    // Do not add abstract class constructor
    // We are just declaring it to python. Because
    // It is an argument type in T800, T1000  constructors
    // and also an argument type of Move() function.
    pybind11::class_<ISpeech>(m, "ISpeech")
        .def_readonly("name", &ISpeech::name)
    ;

    // Add the base class to work polymorphism.
    // For example T800 constructed with ISpeech, if
    // we don't declare it here, python doesn't allow
    // injectign SpeechV1 to T800 constructor.
    pybind11::class_<SpeechV1, ISpeech>(m, "SpeechV1")
        .def(pybind11::init<std::string>()) //Constructor
    ;

    pybind11::class_<SpeechV2, ISpeech>(m, "SpeechV2")
        .def(pybind11::init<std::string>()) // Constructor
    ;

    pybind11::class_<IRobot>(m, "IRobot") // // Abstract, do not add constructor
        .def_readonly("name", &IRobot::name)
        .def("walk", &IRobot::Walk)
        .def("talk", &IRobot::Talk)
    ;

    pybind11::class_<T800, IRobot>(m, "T800")
        .def(pybind11::init<std::string, int, ISpeech &>()) // constructor
        // read-write public data memeber
        // you can use def_readonly as well.
        .def_readwrite("year", &T800::year)
    ;

    pybind11::class_<T1000, IRobot>(m, "T1000")
        .def(pybind11::init<std::string, double, ISpeech &>()) // constructor
        // Define property with getter and setter
        .def_property("height", &T1000::GetHeight, &T1000::SetHeight)
        .def("get_data", &T1000::GetData)
    ;

    m.def("move", &Move);
}
