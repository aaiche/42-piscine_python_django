"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
"""

def apply_modifier(modifier, target):
    """ modifier est une varible mais c est une fonction """
    result = modifier(target)
    return result

if __name__ == '__main__':
    a = 1
    
    """ avec lambda: on declare une fonction anonyme, ie qui n a pas de nom """
    """ cette fonction prend en parametre x et la divise par 2"""
    """ on assigne cette fonction a la variable modifier """
    modifier = lambda x : x / 2

    b = apply_modifier(modifier, a)
    print(b)


    """ L interet des fonctions lambda: c est de declarer des mini fonctions a l interieur de notre code et on peut les utiliser aux fonctions python map et filter"""
