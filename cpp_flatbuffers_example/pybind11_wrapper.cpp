#include <pybind11/pybind11.h>
#include <decode_classification.hpp>

PYBIND11_MODULE(decode_example, m) {
    m.doc() = "pybind11 example plugin"; // Optional module docstring
    m.def("deserialize", &deserialize, "A function which deserializes classification flatbuffers");
}
