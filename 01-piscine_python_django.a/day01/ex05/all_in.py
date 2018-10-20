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

def is_key_present(x, d):
    """ 
        This function is is_key_present()  and it is doing ...
    """
    if x.lower() in (name.lower() for name in d):
        return True
    else:
        return False

def is_value_present(x, d):
    """ 
        This function is is_value_present()  and it is doing ...
    """
    if x.lower() in (name.lower() for name in d.values()):
        return True
    else:
        return False

def get_key_from_dictionnary_using_value_search(search_value, d):
    """ 
        This function is get_capital_city()  and it is doing ...
    """
    for key, value in d.items():
        #print('key:', key, "value:", value)
        if value.lower() == search_value.lower():
            return key
        
    return None

def get_key_from_dictionnary_using_key_search(search_key, d):
    """ 
        This function is get_()  and it is doing ...
    """
    for key, value in d.items():
        #print('key:', key, "value:", value)
        if key.lower() == search_key.lower():
            return key
        
    return None

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

    if len(arguments) != 2:
        sys.exit(-1)

    capitals_or_states = [x.strip() for x in arguments[1].split(',')]
    capitals_or_states = [x for x in capitals_or_states if len(x) > 0]
    #capitals_or_states = [x.lower() for x in capitals_or_states]

    for x in capitals_or_states:
        if is_value_present(x, capital_cities) == True:
            short_name_state = get_key_from_dictionnary_using_value_search(x, capital_cities)
            if short_name_state in states.values():
                full_name_state = get_key_from_dictionnary_using_value_search(short_name_state, states)
                print(capital_cities[short_name_state], 'is the capital of', full_name_state)
            else:
                print(capital_cities[short_name_state], 'is a capital ', 'can not find corresponding state')
        elif is_key_present(x, states) == True:
            full_name_state = get_key_from_dictionnary_using_key_search(x, states)
            short_name_state = states[full_name_state]
            if short_name_state in capital_cities:
                full_name_capital_city = capital_cities[short_name_state]
                print(full_name_capital_city, 'is the capital of', full_name_state)
            else:
                print(fullt_name_state, 'is a state ', 'can not find corresponding capital city')
        else:
            print(x, 'is neither a capital city nor a state')

    sys.exit(0)

if __name__ == '__main__' :
    """ 
    """
    arguments = sys.argv
    main(arguments)

