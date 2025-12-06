from helloworld import firstfunc

firstfunc("meow")


# How the code is executed behind the scenes:
# Python code is first parsed into an AST, then compiled into bytecode by CPython.
# That bytecode is executed by the Python Virtual Machine (PVM), which is built inside CPython.
# The PVM runs each instruction step-by-step while CPython manages memory and objects behind the scenes.
# All of this (parser, compiler, PVM, memory manager) gets installed automatically when you install Python.