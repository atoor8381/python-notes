from helloworld import firstfunc

firstfunc("meow")


# How the code is executed behind the scenes:
# Python code is first parsed into an AST, then compiled into bytecode by CPython.
# That bytecode is executed by the Python Virtual Machine (PVM), which is built inside CPython.
# The PVM runs each instruction step-by-step while CPython manages memory and objects behind the scenes.
# All of this (parser, compiler, PVM, memory manager) gets installed automatically when you install Python.
# when we import something a pycache or something is created is this the bytcode and we do this so that when another change is made to the source code we only make change to the bytcode 
# and we dont have to compile the whole source code to the bytcode again 