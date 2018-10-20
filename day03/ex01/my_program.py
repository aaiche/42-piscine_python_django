from local_lib.path import Path

#ou_est_local_lib_qui_contient_path = "./local_lib/"
quel_est_le_repertoire_de_travail_a_donner_a_path = "."
quel_est_le_fichier_a_creer= "monfichier"

def func():
    my_dir = Path(quel_est_le_repertoire_de_travail_a_donner_a_path) 
    my_dir = my_dir / 'tmp'
    #my_dir = my_dir / 'tmp/tmp' NE MARCHE: je passe a autre chose !!!
    """ est ce dir qu il existe """
    if not my_dir.isdir():
        my_dir.mkdir()

    my_new_file = my_dir / quel_est_le_fichier_a_creer
    """ est que le fichier existe """
    if not my_new_file.isfile():
        my_new_file.touch()

    my_new_file.write_text("\nQuelLe galere ce jour!!!\n")
    print(my_new_file.text())

if __name__ == '__main__':
    func()
