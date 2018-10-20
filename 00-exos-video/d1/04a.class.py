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

    a = "To be or not to be"
    print(a)
    print(type(a))

    b = 1
    print(b)
    print(type(b))

    c = False
    print(c)
    print(type(c))

    """ null dans d autres langages """
    """ meme None est une classe """
    d = None
    print(d)
    print(type(d))

    """ meme le type est une classe """
    print(type(type(a)))
