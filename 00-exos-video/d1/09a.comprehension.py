"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
comprehension:
    ptite particularite de python qui permet de creer des listes de facon concise
"""

if __name__ == '__main__':
    """ """
    l = []
    for i in range(10):
        """ si i est paire"""
        if i % 2 == 0:
            """ i au carree"""
            l.append(i ** 2)
    print(l)

    """ on fait la meme chose ci-dessus en une seule ligne avec les comprehension"""
    """ [...] permet de faire une liste """
    """ ce sera utile pour cette journee """
    """ Les list comprehensions sont des expressions qui permettent de générer des listes d’une manière très compacte 
        L’expression est de la forme :
                [expression for expression in sequence [if test]]
    """

    l = [i ** 2 for i in range(10) if i %2 == 0]
    print(l)

    l = [i ** 2 for i in range(10)]
    print(l)
