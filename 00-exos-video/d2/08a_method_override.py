#!/usr/bin/python3
"""
    Framework Django D01 - 42
    Created on:
    Author
"""
""" 
    modifier le comportement : on appelle cela le polymorphisme
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
class Chicken(Dinosaur):
    """ on ecrase l attribut herite """
    des = "Great camera stabilisator!"

    def __init__(self):
        """ on accede au contructor parent """
        super().__init__()
        print('__init__() of Chicken: It is a chicken!')

    def roar(self):
        print('roar(): cot cot?')

    """ attribut de classe """
    is_extinct = False


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


    print("\nChicken case: ")
    print("- Instantiation :")
    c = Chicken()
    print("- Description :")
    print(c.des)
    print("- Roar :")
    c.roar()
    print("- Is this extinct?")
    print(c.is_extinct)

