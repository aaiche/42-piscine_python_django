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

def list_type():
    """ list est un type mutable """
    """ list c est comme un tableau"""
    my_list = ['a', 'b', 'c']
    print("my_list : ", my_list)
    my_list = list()
    print("my_list : ", my_list)
    my_list.append('a')
    print("my_list : ", my_list)
    my_list.append(2)
    print("my_list : ", my_list)
    my_list.append(3.0)
    print("my_list : ", my_list)
    print("my_list[2] : ", my_list[2])

def tuple_type():
    """ je pense que c est immuable """
    my_tuple = tuple()
    print("my_tuple : ", my_tuple)
    my_tuple = (1, 'b', 3.0)
    print("my_tuple : ", my_tuple)
    print("my_tuple[2] : ", my_tuple[2])


def range_type():
    """ definir un intervalle numerique de nbres, seulement les nombres """
    """ c est immuable """
    """ range ne contient pas vraiment ttees les valeurs, mais seulement le point de de depart et celui d arrivee. Et pour l imprimer: il faut le convertir en liste"""

    """ entre 0 et 4 """
    my_range = range(5)
    print("my_range : ", my_range)
    print("my_range : ", list(my_range))

    """ entre 2 et  5 exclu"""
    my_range = range(2, 5)
    print("my_range : ", my_range)
    print("my_range : ", list(my_range))

    """ entre  et  """
    my_range = range(2, 10, 2)
    print("my_range : ", my_range)
    print("my_range : ", list(my_range))





if __name__ == '__main__':
    list_type()
    print('\n')


    tuple_type()
    print('\n')

    range_type()
    print('\n')

