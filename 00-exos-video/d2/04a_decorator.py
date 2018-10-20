#!/usr/bin/python3
"""
    Framework Django D01 - 42
    Created on:
    Author
"""
import datetime

""" 
    Decorator: notion un specifique a python
    un Decorator est une fonction qui:
        - prend en parametre une autre fonction
        - retourne une version un ptit peu modifie
    un Decorator, c est juste une fonction qui va modifier le comportement d autres fonctions
"""

# Row function
""" fonction temoin """
def raw_function(s):
    return s

# With decorators
""" defintion du decorator """
def decorator(f):
    """ input: f est une fonction """
    def mafunction(s):
        """ datetime.datetime.now().__str__() : heure et date """
        return (datetime.datetime.now().__str__() + ' ' + f(s))

    """ output: mafunction est une fonction """
    return mafunction

""" 1ere utilisation -- 1ERE SYNTAXE : """ 
""" cette fonction est similiare a la fonction temoin """
def dec_function_assign(s):
    return s

""" ON REDEFINIT la fonction dec_functio_assign """
""" ce sera une fonction decoree apres passage dans le decorator """
dec_function_assign = decorator(dec_function_assign)


""" 2ere utilisation -- 2EME SYNTAXE : un peu plus facile """
""" cette fonction est similiare a la fonction temoin """
""" avec @decorator, pyhton fera la decoration """
@decorator
def dec_function_def(s):
    return s

# ---------------------------------------------------------------------------

if __name__ == '__main__' :
    """ """
    print('Without decorator :')
    print(raw_function('foo'))

    print('\nWith decorator (decorated function as variable) :')
    print(dec_function_assign('foo'))

    print('\nWith decorator (@ symbol) :')
    print(dec_function_assign('foo'))
