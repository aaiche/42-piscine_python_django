"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
    la premiere ligne est une condition qui ouvre un bloc.
    le bloc est ce qui indente
"""
if __name__ == '__main__' :
    """ declaration d une string beatles """
    beatles = "Hey Jude, don't make it bad"
    print(beatles)
    print(beatles[0])
    print(beatles[1])
    print(beatles[2])
    print(beatles[4:8])

    """ ne fonctionne pas : les strings sont declarees de facon immutable. """
    """ impossible de modifier un carctere d une string comme on le ferait dans un tableau en C """
    #beatles[0] = 'Z'
    """ Si on veut modifier une string: cela va passer forcement par la copie de cette string """

