#!/usr/bin/python3
"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
"""
class Foo:
    pass    # do nothing. and used to denote a empty body. Sinon on a une erreur de syntaxe

class Bar:
    pass

if __name__ == '__main__' :
    """ on instancie la classFoo """
    f = Foo()
    b = Bar()

    """ Meme une variable, c est un objet qui est instancie a partir d une autre class """
    i = int(1)

    print(type(f))
    print(type(b))
    print(type(i))
