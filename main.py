from app import misc, db, user
import os, webbrowser
from datetime import datetime


#  Vérification de l'existence de la base de donnée
misc.app = db.check_db()
if misc.app:
    user.check_default()
    global current_user
    current_user = user.user_login()

#  Vérification du dernier login 


def menu(menu: str):
    os.system("clear")
    if menu in ['Q']:
        if misc.prompt_yes_no("Etes-vous sûr de vouloir quitter l'application ?"): misc.app = False
    elif menu == "C":
        global current_user
        current_user = user.user_login()
    elif menu == 'R':
        user.search_user()
    elif menu == 'P':
        user.change_passwd(current_user['user_id'])
    elif menu == "Z":
        webbrowser.open('https://github.com/milkshake308/Gestion_Utilisateurs_AH')  
    elif menu == "A" and current_user['group_name'] == 'admins':
        user.user_add()
    elif menu == "T" and current_user['group_name'] == 'admins':
        # Execution du scénario de test voulu
        pass
    else:
        print("Veuillez saisir une option valide !")

while(misc.app == True):
    os.system("clear")
    print("########## MENU PRINCIPAL ##########\n")
    print("Q. Quitter l'application")
    print("C. Changer d'utilisateur")  
    print("P. Changer de mot de passe")
    print("R. Rechercher un utilisateur")
    print("Z. Voir le github")

    if current_user['group_name'] == 'admins':
        print("A. Ajouter un utilisateur")
        print('T. Executer un test')

    current_time = datetime.now()
    time_diff = current_time - current_user['password_update']
    seconds_to_check = 120
    if time_diff.total_seconds() >  seconds_to_check:
        print(f"\nVotre mot de passe n'a pas été changé depuis plus de {seconds_to_check}s !\n")
    
    
    print("\nBienvenue, ", current_user['firstname'])
    menu(input("Choix du menu (ex: 'Q') : "))