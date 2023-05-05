# Tasks to build and test pybind11 wrapper for classification flatbuffer decoding
# Started May 2023
# Alex
import pathlib
import sys
import os
import shutil
import re
import glob
from invoke import task, run
import inspect

#https://github.com/pyinvoke/invoke/issues/833
if not hasattr(inspect, 'getargspec'):
    inspect.getargspec = inspect.getfullargspec


@task
def clean(c):
    """Remove any built objects"""
    print_banner("Cleaning previous builds")
    for file_pattern in (
        "*.o",
        "*.so",
        "*.obj",
        "*.dll",
        "*.exp",
        "*.lib",
        "*.pyd",
    ):
        for file in glob.glob(file_pattern):
            os.remove(file)


def print_banner(msg):
    print("==================================================")
    print("= {} ".format(msg))


@task
def setenv(c):
    c.run("export BOOST=/workspace/boost_1_82_0")


@task(setenv)
def decoder(c):
    """Build the shared library for the sample C++ code"""
    print_banner("Building C++ Library")
    c.run(
        "g++ -O3 -Wall -shared -fPIC decode_classification.cpp "
        "-o libdecoder.so -I$BOOST"
    )
    print("* Complete")


def compile_python_module(cpp_name, extension_name):
    run(
        "g++ -O3 -Wall -Werror -shared -fPIC "
        "`python3 -m pybind11 --includes` "
        "-I . "
        "{0} "
        "-o {1}`python3-config --extension-suffix` "
        "-L . -ldecoder -Wl,-rpath,.".format(cpp_name, extension_name)
    )


@task(decoder)
def wrapper(c):
    """Build the pybind11 wrapper library"""
    print_banner("Building PyBind11 Module")
    compile_python_module("pybind11_wrapper.cpp", "decode_example")
    print("* Complete")


@task(wrapper)
def testwrapper(c):
    print_banner("Testing PyBind11 Module")
    c.run("python decoder_test.py", pty=True)


@task(
    clean,
    testwrapper,
)
def all(c):
    pass