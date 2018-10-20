#!/usr/bin/python3
"""
    Framework Django D01 - 42
    Created on:
    Author
"""
""" 
"""
import random
#from beverages import *
import beverages

class CoffeeMachine:
    """ attributs de classe"""
    """ atribut relatf a la classe Foo et non plus relatif a l instance """
    counter = 0

    def __init__(self):
        """ lors de l instanciation de CoffeeMachine, comme increment_counter() n existe pas 
        dans le corps de l objet, il ira le checher dans la classe """
        self.reset_counter()
        #print("CoffeeMachine instance created. Number of served co : %d]." % self.counter)

    class EmptyCup(beverages.HotBeverage):
        """ attributs de classe"""
        price = 0.90
        name = "empty cup"
        def description(self):
            return("An empty cup?! Gimme my money back!")

    class BrokenMachineException(Exception):
        """ lèvera juste une exception """
        #https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python
        #message = "This coffee machine has to be repaired."
        #def __init__(self, message):
            # Call the base class constructor with the parameters it needs
            #super().__init__(message)
            # Now for your custom code...
            #self.errors = errors
        def __init__(self, msg="This coffee machine has to be repaired."):
            super().__init__(self, msg)

    def repair(self):
        self.reset_counter()

    def serve(self, beverage):
        """ is b n est pas de type HotBeverage, je leve une exception """
        try:
            if not isinstance(beverage, beverages.HotBeverage):
                """ l exception va provoquer une erreur """
                raise Exception("I don't have this!")
            #else:
            #   print("Miam!:")
        except Exception as e:
            print(e)

        self.increment_counter()
        if self.get_counter() > 10:
            # tombe en panne
            #print("machine en panne %d servis" % self.get_counter())
            raise self.BrokenMachineException()
        else:
            #print("machine en service %d servis" % self.get_counter())
            if random.choice([True, False]):
                instance = beverage
                return instance
            else:
                instance = self.EmptyCup()
                return instance

    def check_random_function(self):
        if random.choice([True, False]):
            print('True')
        else:
            print('False')

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

    @classmethod
    def get_counter(cls):
        return(cls.counter)

    @classmethod
    def reset_counter(cls):
        cls.counter = 0

# ---------------------------------------------------------------------------

if __name__ == '__main__' :
    """ tests """

    coffee_machine_instance = CoffeeMachine()
    try:
        for i in range(42):
            b = coffee_machine_instance.serve(beverage = random.choice([
                beverages.Coffee(),
                beverages.Tea(),
                beverages.Chocolate(),
                beverages.Cappuccino()
            ]))
            print(b.name)
    except Exception as e:
        print (e)
        coffee_machine_instance.repair()

    try:
        for i in range(42):
            b = coffee_machine_instance.serve(beverages.Coffee())
            print(b.name)
    except Exception as e:
        print(e)
