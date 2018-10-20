#!/usr/bin/python3
"""
    Framework Django D01 - 42
    Created on:
    Author
"""

""" 
    on importe le module sys
"""
import sys
import antigravity

""" 
    global variables
"""

def main(argv):
        seq = (argv[3],argv[4])
        s = "-".join(seq)
        #antigravity.geohash(float(argv[1]), float(argv[2]), bytes(s, 'utf-8'))
        print('s=', s)
        antigravity.geohash(float(argv[1]), float(argv[2]), b's')

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print('usage: ./geohashing.py <votre location> <date> <la valeur la plus recente du dow jones de date>')
        print('        <votre location>:  latitude longitude')
        print()
        print('exple: ./geohashing 37.421542 -122.085589 2005-05-26 10458.68')

        print('Je ne comprends pas cet exercice !!! ai essaye plusieurs fois avec la localisation de 42')
        print('Mais renvoie a perpette alors qu il est suppose me donner des endroits proches de 42!!!!!!')
        print()
        print('voici un exple utilise dans le web ....')
        print('     e1r7p22% ./geohashing.py 37.421542 -122.085589 2005-05-26 10458.68')
        print('         37.857713 -122.544543')
        sys.exit(1)

    #main(sys.argv)
        
    argv = sys.argv
    seq = (argv[3],argv[4])
    s = "-".join(seq)
    antigravity.geohash(float(argv[1]), float(argv[2]), bytes(s, 'utf-8'))


