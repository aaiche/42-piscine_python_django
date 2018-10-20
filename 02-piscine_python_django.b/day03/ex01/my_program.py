#
# import Path from local_lib.path module directory
# cf. exemple dans ./local_lib/path.py
#
from local_lib.path import Path

def func():
    dossier_a_creer = "nouveau_dossier"
    fichier_a_creer= "nouveau_fichier.txt"

    my_dir = Path(dossier_a_creer) 
    #my_dir = my_dir / 'tmp'
    #my_dir = my_dir / 'tmp/tmp' NE MARCHE: je passe a autre chose !!!
    """ est ce dir qu il existe """
    if not my_dir.isdir():
        my_dir.mkdir()

    my_new_file = my_dir / fichier_a_creer
    """ est que le fichier existe """
    if not my_new_file.isfile():
        my_new_file.touch()

    my_new_file.write_text("\n1ere piscine python: QuelLe galere ce jour!!!\n2eme piscine python: Cela va un peu mieux...\n\n")
    print(my_new_file.text())

if __name__ == '__main__':
    func()
