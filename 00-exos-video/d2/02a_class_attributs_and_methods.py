#!/usr/bin/python3
"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
"""
class Car:
    """ self sera tjrs le 1er parametre, et devra etre tjrs present dans les methodes """
    """ represente l instance courante, i.e. l instance a partir de laquelle on appelle la methode """
    """ equivalent de this dans php """
    def drive(self):
        print('Vroom !')

    """ self est """
    def paint(self, color):
        self.color = color      # ici on definit un attribut color
        print('%s is now the new color' % str(color))

    def get_color(self):
        return self.color


if __name__ == '__main__' :
    """ on instancie la class Car dans une variable x """
    x = Car()
    print('Drive method called :')

    """ Les méthodes définies dans les classes ont donc toujours un premier paramètre
        fourni de manière transparente par l’interpréteur, x.drive() étant remplacé au
        moment de l’exécution par Car.drive(x).
        
        On comprend par cette notation que le code défini dans la classe Car est partagé par
        toute les instances et que seuls les attributs de données instanciés dans les méthodes
        restent spécifiques aux instances.
    """
    x.drive()

    print('\nChanging attribute value with a setter :')
    x.paint('red')
    print('\nPrint getter retun :')
    print(x.get_color())

    print('\nDirect access to attribute :')
    x.color = 'blue'
    print(x.get_color())

