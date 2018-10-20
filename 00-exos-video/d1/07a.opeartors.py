"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
"""

def math_operators():
    print(5 - 1)
    print(2 + 1.0)
    print(1 * 2)

    """ resultat en reel """
    print(42 / 41)

    """ resultat en int """
    print(42 // 42)

    print(42 % 42)

def comparison_operators():
    print(1 == 2)
    print(1 != 2)
    print(1 > 2)
    print(1 < 2)
    print(1 >= 2)
    print(1 <= 2)

def concatenations_operators():
    print("FUUUUUUU" + "SIOOOOOOOOON !!")

    """ on ne peut concatener en python des types differents aux strings"""
    """ python ne va as converitr 0 en string '0' """
    print(0 + "This will fail miseraby.")


if __name__ == '__main__':
    """ """
    math_operators()
    print()

    comparison_operators()
    print()

    concatenations_operators()
    print()
