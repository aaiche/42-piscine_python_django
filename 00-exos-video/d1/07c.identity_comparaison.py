"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
"""

if __name__ == '__main__':
    """ """
    a = int(1)
    b = float(1)
    print(' a of type: ', type(a), ' and value:', a)
    print(' b of type: ', type(b), ' and value:', b)
    print()


    """ """
    if a == b :
        print('a has the same value as b')
    else:
        print('a has NOT the same value as b')

    print()
    """ est ce que les 2 objects sont identiques """
    """ se mefier de is """
    if a is b :
        print('a is the same object as b')
    else:
        print('a is NOT the same object as b')

