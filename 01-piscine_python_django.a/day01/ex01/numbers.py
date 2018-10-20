"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
"""
def display_numbers(numbers_file):
    """ 
        This function is display_numbers()  and it is doing ...
    """
    """ with : il nous assure que le fichier sera ferme """
    with open(filename, 'r') as f:
        for line in f:
            line2 = line.replace(',', '\n')
            print(line2.strip())

if __name__ == '__main__' :
    """ 
    """
    filename = 'numbers.txt'
    display_numbers(filename)

