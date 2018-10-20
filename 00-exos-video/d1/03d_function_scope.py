"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
"""
global_var = "This var is in the global module namespace"

def my_function():
    local_func_var = 'This variable is in the function namespace'

    def inner_function():
        enclosed_func_var = 'This variable is in the enclosed function namespace'
        print('[inner_function] - ', global_var)
        print('[inner_function] - ', local_func_var)
        print('[inner_function] - ', enclosed_func_var, '\n')

    inner_function()

    print('\n')

    print('[my_function] - ', global_var)
    print('[my_function] - ', local_func_var, '\n')
    #print('[my_function] - ', enclosed_func_var, '\n')

if __name__ == '__main__':
    my_function()

    print('\n')

    print('[global_scope] - ', global_var, '\n')
    #print('[global_scope] - ', local_func_var, '\n')
    #print('[global_scope] - ', enclosed_func_var, '\n')
