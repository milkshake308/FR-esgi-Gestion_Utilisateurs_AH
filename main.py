from app import misc, db
import os



#  Vérification de l'existence de la base de donnée
misc.app = db.check_db()

def menu(menu: str):
    os.system("clear")
    if menu == "0":
        if misc.prompt_yes_no("Etes-vous sûr de vouloir quitter l'application ?"): misc.app = False
    elif menu == "2":
        print("néant absolu")
    else:
        print("Veuillez saisir une option valide !")

while(misc.app == True):
    os.system("clear")
    print("########## MENU PRINCIPAL ##########")
    print("0. Quitter l'application")
    menu(input("Choix du menu (ex: '0') : "))