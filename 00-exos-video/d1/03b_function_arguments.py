"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
"""

def my_function():
    print('...alwayas look on the bright side')

def my_function2(argument):
    print(argument)

def my_function3(argument='(Whistle)'):
    print(argument)

def my_function4(argument, argument2):
    print(argument, argument2)

if __name__ == '__main__':
    my_function()
    my_function2(' of life...')
    my_function3()
    my_function4(argument2 = ' of life...', argument='Always look on the light side')
