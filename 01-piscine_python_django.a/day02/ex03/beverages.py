#!/usr/bin/python3
"""
    Framework Django D01 - 42
    Created on:
    Author
"""
""" 
"""

class HotBeverage:
    """ attributs de classe"""
    price = 0.30
    name = "hot beverage"

#    def __init__(self):
#        """ Question ? est ce on peut overrider les attributs d instnce """
#        self.price = 0.30
#        self.name = "hot beverage"

    def description(self):
        return("Just some hot water in a cup.")

    def __str__(self):
        m  = 'name : "%s"' % self.name
        m += "\nprice : %.2f" % self.price
        m += "\ndescription : \"%s\"" % self.description()
        return m

class Coffee(HotBeverage):
    """ attributs de classe"""
    price = 0.40
    name = "coffee"

class Tea(HotBeverage):
    """ attributs de classe"""
    name = "tea"

class Chocolate(HotBeverage):
    """ attributs de classe"""
    price = 0.50
    name = "chocolate"

    def description(self):
        return("Chocolate, sweet chocolate...")

class Cappuccino(HotBeverage):
    """ attributs de classe"""
    price = 0.45
    name = "cappuccino"

    def description(self):
        return("Un po’ di Italia nella sua tazza!")


# ---------------------------------------------------------------------------

if __name__ == '__main__' :
    """ tests """
    hotbeverage_instance = HotBeverage()
    #print(hotbeverage_instance)
    #print()

    coffee_instance = Coffee()
    #print(coffee_instance)
    #print()

    tea_instance = Tea()
    #print(tea_instance)
    #print()

    chocolate_instance = Chocolate()
    print(chocolate_instance)
    print()

    cappuccino_instance = Cappuccino()
    print(cappuccino_instance)
    print()

