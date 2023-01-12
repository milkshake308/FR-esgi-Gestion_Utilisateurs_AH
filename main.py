from app import misc
import os
global app 

app = True

def menu(menu: str):
    os.system("clear")
    if menu == "0":
        global app
        if misc.prompt_yes_no("Etes-vous sûr de vouloir quitter l'application ?"): app = False
    elif menu == "2":
        print("néant absolu")
    else:
        print("Veuillez saisir une option valide !")

while(app):
    print("########## MENU PRINCIPAL ##########")
    print("0. Quitter l'application")
    menu(input("Choix du menu (ex: '0') : "))