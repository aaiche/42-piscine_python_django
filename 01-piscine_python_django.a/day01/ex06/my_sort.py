"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
    on importe le module sys
"""
#import sys

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

def main():
    """ 
        This function is main()  and it is doing ...
    """
    d = {
        'Hendrix'   :   '1942',
        'Allman'    :   '1946',
        'King'      :   '1925',
        'Clapton'   :   '1945',
        'Johnson'   :   '1911',
        'Berry'     :   '1926',
        'Vaughan'   :   '1954',
        'Cooder'    :   '1947',
        'Page'      :   '1944',
        'Richards'  :   '1943',
        'Hammett'   :   '1962',
        'Cobain'    :   '1967',
        'Garcia'    :   '1942',
        'Beck'      :   '1944',
        'Santana'   :   '1947',
        'Ramone'    :   '1948',
        'White'     :   '1975',
        'Frusciante':   '1970',
        'Thompson'  :   '1949',
        'Burton'    :   '1939',
    }

    # d.items() va donner une liste de tuple
    # la fonction anonyme va etre passe au comprateur, ie le 2eme arg du tuple = egale date de naissance
    #l = sorted(d.items(), key=lambda x: x[1])
    # l devient une liste et donc on passe .... je ne comprends ce sort !!! 
    #l = sorted(l, key=lambda x: x[1])
    #for tup in l:
        #print(tup[0], ':', tup[1])
        #print(tup[0])

    #http://www.compciv.org/guides/python/fundamentals/sorting-collections-with-sorted/
    def foo4(x):
        return (x[1], x[0])
    l = sorted(d.items(), key=foo4)
    for tup in l:
        #print(tup[0], ':', tup[1])
        print(tup[0])

if __name__ == '__main__' :
    """ 
    """
    main()

