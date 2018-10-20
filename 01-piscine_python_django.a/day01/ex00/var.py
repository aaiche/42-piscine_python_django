"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
"""
def my_var():
    """ 
        This function is my_var()  and it is doing ...
    """
    for elt in [42, '42', 'quarante-deux', 42.0, True, [42], {42: 42}, (42, ), set()]:
        print(elt, 'est de type', type(elt))

if __name__ == '__main__' :
    """ 
    """
    my_var()
