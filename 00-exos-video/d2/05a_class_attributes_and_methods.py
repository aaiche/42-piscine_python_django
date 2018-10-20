#!/usr/bin/python3
"""
    Framework Django D01 - 42
    Created on:
    Author
"""
""" 
"""

class Foo:
    """ atribut relatf a la classe Foo et non plus relatif a l instance """
    counter = 0

    def __init__(self):
        print("\n__init__()")
        """ lors de l instanciation de Foo, comme increment_counter() n existe pas dans le corps de l objet, il ira le checher dans la classe """
        self.increment_counter()
        print("Foo instance created. Number of instance : %d]." % self.counter)

    def __del__(self):
        print("\n__del__()")
        self.decrement_counter()
        print("Foo instance deleted. Number of instance : %d]." % self.counter)

    """
        @classmethod
        Convertit une simple fonction en une méthode de classe. Une méthode de classe est
        une méthode qui est associée à une classe et non à ses instances. Elle peut donc être
        appelée depuis la classe ou depuis n’importe quelle instance, sachant que dans tous
        les cas, le premier paramètre implicite est la classe et non l’instance.
    """
    @classmethod
    def increment_counter(cls):     # on passe directement la classe en parametre
        cls.counter += 1

    @classmethod
    def decrement_counter(cls):
        cls.counter -= 1


# ---------------------------------------------------------------------------

if __name__ == '__main__' :
    """ """
    a = Foo()
    del a

    a = Foo()
    b = Foo()
    c = Foo()

    del b
    b = Foo()



