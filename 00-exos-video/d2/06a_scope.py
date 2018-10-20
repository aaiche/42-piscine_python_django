#!/usr/bin/python3
"""
    Framework Django D01 - 42
    Created on:
    Author
"""
""" 
"""

class Bar:
    """ """
    des = 'Bar in main'

class Foo:
    """ """
    des = 'Foo in main'

    class Bar:
        des = 'Bar in Foo'

    class Foo:
        def method(self):
            print("This is a method in Foo.Foo")


# ---------------------------------------------------------------------------

if __name__ == '__main__' :
    """ """
    print("Description of Bar in main scope :")
    print("- From class :")
    print(Bar.des)
    print("- From instance :")
    b = Bar()
    print(b.des)


    """ """
    print("\nDescription of Bar in Foo scope :")
    print("- From class :")
    print(Foo.Bar.des)
    print("- From instance :")
    fb = Foo.Bar()
    print(fb.des)


    """ """
    print("\nMethod class (method() from Foo.Foo instance) :")
    ff = Foo.Foo()
    ff.method()

