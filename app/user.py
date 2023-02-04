import login
import passwd
def user_add():
    nom = input("Entrez votre nom svp : ")
    prenom = input("Entrez votre prenom svp : ")
    passwds = passwd.generate_passwd()
    print("Votre login est : " + login.generate_login(nom, prenom))
    print("Votre Mot de passe est : " + passwds[0])
    print("Le hash du mot de passe est : " + passwds[1])


user_add()