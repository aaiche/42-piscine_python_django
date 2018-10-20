"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
"""

if __name__ == '__main__':
    base_string = "{0} bites the {1}"
    print(base_string)
    new_string = base_string.format('Another one', 'dust')
    print(new_string)

    print('\n')

    base_string = "{who} bites the {what}"
    print(base_string)
    new_string = base_string.format(what='another one', who='dust')
    print(new_string)

    print('\n')

    base_string = "%s bites the %s"
    print(base_string)
    new_string = base_string%('She', ' life to the fullest')
    print(new_string)
