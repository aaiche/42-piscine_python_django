"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
"""

if __name__ == '__main__':
    """ """
    filename = 'my_file.txt'

    """ with : il nous assure que le fichier sera ferme """
    with open(filename, 'r') as f:
        for line in f:
            print(line)
    
