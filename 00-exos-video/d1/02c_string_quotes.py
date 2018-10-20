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
    a = 'I can put double quotes    " <-- like this --> " '
    print(a)

    a = "I can put simple quotes    ' <-- like that --> ' "
    print(a)

    a = """
'I can put what I "want' and carriage returns are ...
        presserved'.
    """
    print(a)

    a = '''
        'I can put what I "want' and carriage returns are ...
        AGAIN, presserved'.
    '''
    print(a)

