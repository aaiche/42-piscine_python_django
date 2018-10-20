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
            raise Exception("I don't like this!")       # le 
        else:
            print("Miam!")


# ---------------------------------------------------------------------------

if __name__ == '__main__' :
    """ """
    h = Human()
    h.eat(Fries())
    try:
        """ ce code va etre executer """
        h.eat(Vegetables())
    except Exception as e:     # Si il y a une exceptin qui est levee, elle va etre attrapee par le code ci-dessous
        print(e)

    print('test')
