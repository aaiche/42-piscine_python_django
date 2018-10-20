#!/usr/bin/python3
"""
    Framework Django D01 - 42
    Created on:
    Author
"""
""" 
"""

class Vegetables:
    pass

class Fries:
    pass

""" """
class Human:
    def eat(self, food):
        """ is food est de type Vegetables, je leve une exception """
        if isinstance(food, Vegetables):
            """ l exception va provoquer une erreur """
            raise Exception("I don't like this!")
        else:
            print("Miam!")


# ---------------------------------------------------------------------------

if __name__ == '__main__' :
    """ """
    h = Human()
    h.eat(Fries())
    h.eat(Vegetables())
    print('test')
