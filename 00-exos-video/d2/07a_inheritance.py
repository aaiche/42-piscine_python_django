#!/usr/bin/python3
"""
    Framework Django D01 - 42
    Created on:
    Author
"""
""" 
"""

class Dinosaur:
    """ attribut de classe """
    des = 'All my friends are dead. :('

    def __init__(self):
        print('__init__() of Dinosaur: A dinosaur appeared!')

    def roar(self):
        print('roar(): ROAARRR!')

    """ attribut de classe """
    is_extinct = True



""" TRex herite de la classe Dinosaur """
""" Dinosaur est la classe parente """
""" important a comprendre:
    TRex est un TRex, mais aussi est aussi un Dinosaur
    les instances de TRex seront egalement des instances de Dinosaur
"""
class TRex(Dinosaur):
    """ on ecrase l attribut herite """
    des = "If you're happy clap your... oh, nevermind."


# ---------------------------------------------------------------------------

if __name__ == '__main__' :
    """ """
    print("Dinosaur case: ")
    print("- Instantiation :")
    d = Dinosaur()
    print("- Description :")
    print(d.des)
    print("- Roar :")
    d.roar()
    print("- Is this extinct?")
    print(d.is_extinct)


    print("\nTRex case: ")
    print("- Instantiation :")
    t = TRex()
    print("- Description :")
    print(t.des)
    print("- Roar :")
    t.roar()
    print("- Is this extinct?")
    print(t.is_extinct)

