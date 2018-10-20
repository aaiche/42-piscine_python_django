"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
    on importe le module sys
"""
import sys

""" 
    global variables
"""

def my_sort(el1, el2):
    """ 
        This function is my_sort()  and it is doing ...
    """
    if el1 > el2:
        return -1
    if el2 < el2:
        return 1
    return 0

def convert_list_of_tuples_into_a_dictionary(l):
    """ 
        This function is convert_list_of_tuples_into_a_dictionary()  and it is doing ...
    """
    d = {}
    for key, value in l:
        d.setdefault(value, []).append(key)
    return d

def display_dictionary(d):
    """ 
        This function is display_dictionary()  and it is doing ...
    """
    for a in d:
        print(a, ":", end = " ")
        for b in d[a]:
            print(b, end = " ")
        print()

def is_key_present(x, d):
    """ 
        This function is is_key_present()  and it is doing ...
    """
    if x in d:
        return True
    else:
        return False

def is_value_present(x, d):
    """ 
        This function is is_key_present()  and it is doing ...
    """
    if x in d.values():
        return True
    else:
        return False

def get_key_from_dictionnary(search_value, d):
    """ 
        This function is get_capital_city()  and it is doing ...
    """
    for key, value in d.items():
        #print('key:', key, "value:", value)
        if value == search_value:
            return key
        
    return None

def display_capital_city(short_name_state, d):
    """ 
        This function is get_capital_city()  and it is doing ...
    """
    if is_key_present(short_name_state, d) == False:
        print('Unknown short_name state')
        sys.exit(-1)
    else:
        capital_city = d[short_name_state]

    print(capital_city)
    sys.exit(0)

def main(arguments):
    """ 
        This function is main()  and it is doing ...
    """
    states = {
        "Oregon"    : "OR",
        "Alabama"   : "AL",
        "New Jersey": "NJ",
        "Colorado"  : "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    #print('arguments %s' %arguments)
    #print("This is the name/path of the script:"), arguments[0]
    #print("Number of arguments:", len(arguments))
    #print("Argument List:", str(arguments))

    if len(arguments) != 2:
        sys.exit(-1)

    capital_city = arguments[1]
    if is_value_present(capital_city, capital_cities) == False:
        print('Unknown capital city')
        sys.exit(-1)

    short_name_state = get_key_from_dictionnary(capital_city, capital_cities)
    #print('short_name_state=', short_name_state)
    if is_value_present(short_name_state, states) == False:
        print('Unknown country short name')
        sys.exit(-1)
    full_name_state = get_key_from_dictionnary(short_name_state, states)
    print(full_name_state)
    sys.exit(0)

if __name__ == '__main__' :
    """ 
    """
    arguments = sys.argv
    main(arguments)

