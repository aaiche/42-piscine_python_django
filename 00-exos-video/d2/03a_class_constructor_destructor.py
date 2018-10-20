#!/usr/bin/python3
"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
"""
class Warrior:
    """ Bob est une valeur par defaut"""
    def __init__(self, name='Bob'):
        self.name = name
        print("Constructor: __init__(): A warrior apeared! His name is %s." % name)

    def __del__(self):
        print("Destructor: __del__(): %s just died." % self.name)



if __name__ == '__main__' :
    """ instance bob est cree et ON EST SURE que l attribut name existe"""
    bob = Warrior()

    tom = Warrior('Tom')

    """ deconseille """
    del tom

    print("\nnote: Bob est detruit par le grabage collector")

