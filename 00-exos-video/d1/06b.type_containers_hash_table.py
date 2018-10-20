"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
    2 type de base: les containers
    un container est une collection d objets. 
    on divise les collections d objets en 2 categories:
        - les sequences
        - les hash maps
"""

if __name__ == '__main__':
    """ cela fonctionne avc le principe cle valeur """
    """ le type dict est muable """
    """ le type dict n est pas ordonnee """
    my_dict = {'type':'dictionnary'}
    print('my_dict: ', my_dict)
    print('\n')

    my_dict = dict()
    print('my_dict: ', my_dict)
    print('\n')

    my_dict['type'] = 'ppictionnary'
    print('my_dict: ', my_dict)
    print('\n')

    print(my_dict['type'])
    print('\n')
