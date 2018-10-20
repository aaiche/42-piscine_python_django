#!/usr/bin/python3

""" This is the desctription of the module/. """

var = "This is a variable"

class Foo:
    """ Foo class description. """

    def __str__(self):
        """ Foo.__str__() method description. """
        return("This is a Foo instance")

def function1():
    """ function1 description. """
    print("This is call of function1()")

def function2(param: int)-> str :
    """ function2 description. It takes an int and returns a str. """
    print("This is call of function2()")
    return str(param)

