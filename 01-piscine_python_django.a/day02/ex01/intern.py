#!/usr/bin/python3
"""
    Framework Django D01 - 42
    Created on:
    Author
"""
""" 
"""

class Intern:
    """ blah """

    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        print("\t__init__(): assigne valeur a attribut Name")
        self.Name = name
        print("\tIntern instance created avec attribut Name:", self.Name)

    def __str__(self):
        """ Intern.__str__() method description. """
        """ return Name de l instance """
        return ("\t" + self.Name)

    def work(self):
        """ lèvera juste une exception """
        raise Exception("\tI’m just an intern, I can’t do that...")

    def make_coffee(self):
        """ lèvera juste une exception """
        c = self.Coffee()
        return c

    class Coffee:
        #php __toString():
        #   permet de serialiser = transformer une instance en une chaine de characteres
	#   Methode speciale tres pratique qd on veut debuger ou faire du log
	#   permet de serialiser = transformer une instance en une chaine de characteres
        def __str__(self):
            return "\t" + "Coffee(): This is the worst coffee you ever tasted."


""" version sans commentaire """
class Intern2:
    """ blah """

    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.Name = name

    def __str__(self):
        return (self.Name)

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        c = self.Coffee()
        return c

    class Coffee:
        #php __toString():
        #   permet de serialiser = transformer une instance en une chaine de characteres
	#   Methode speciale tres pratique qd on veut debuger ou faire du log
	#   permet de serialiser = transformer une instance en une chaine de characteres
        def __str__(self):
            return "This is the worst coffee you ever tasted."


# ---------------------------------------------------------------------------

if __name__ == '__main__' :
    """ tests """
    
    print("--------------------------------------")
    print("- version commentee                   ")
    print("--------------------------------------")
    print("Instancier 1 fois la classe Intern sans parametre:")
    a = Intern()
    print("Convertir l instance cree en une string")
    print(a)
    print()

    print("Instancier 1 fois la classe Intern avec name = Mark:")
    m = Intern('Mark')
    print("Convertir l instance cree en une string")
    print(m)
    print()

    print("Demandez à Mark de vous make_coffee():")
    print("   En demanant un cafe, on a colle a l'instance mark, une nouvelle instance Coffee.")
    print("Convertir l instance cree en une string")
    print(m.make_coffee())
    print()

    print("Demandez à Autre de work():")
    print("     work() leve une exception que l on doit attraper")

    try:
        """ ce code va etre executer """
        a.work()
    except Exception as e:     # Si il y a une exceptin qui est levee, elle va etre attrapee par le code ci-dessous
        print(e)
    print()


    print("--------------------------------------")
    print("- version non commentee                   ")
    print("--------------------------------------")
    a = Intern2()
    print(a)

    m = Intern2('Mark')
    print(m)

    print(m.make_coffee())

    try:
        """ ce code va etre executer """
        a.work()
    except Exception as e:     # Si il y a une exceptin qui est levee, elle va etre attrapee par le code ci-dessous
        print(e)

