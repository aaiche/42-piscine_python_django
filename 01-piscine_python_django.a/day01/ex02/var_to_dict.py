"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
    global variable
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

def main():
    """ 
        This function is main()  and it is doing ...
    """
    d = [
        ('Hendrix'   , '1942'),
        ('Allman'    , '1946'),
        ('King'      , '1925'),
        ('Clapton'   , '1945'),
        ('Johnson'   , '1911'),
        ('Berry'     , '1926'),
        ('Vaughan'   , '1954'),
        ('Cooder'    , '1947'),
        ('Page'      , '1944'),
        ('Richards'  , '1943'),
        ('Hammett'   , '1962'),
        ('Cobain'    , '1967'),
        ('Garcia'    , '1942'),
        ('Beck'      , '1944'),
        ('Santana'   , '1947'),
        ('Ramone'    , '1948'),
        ('White'     , '1975'),
        ('Frusciante', '1970'),
        ('Thompson'  , '1949'),
        ('Burton'    , '1939')
    ]
    #create a list
    #l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
    dd = {}
    dd = convert_list_of_tuples_into_a_dictionary(d)
    display_dictionary(dd)


if __name__ == '__main__' :
    """ 
    """
    main()

