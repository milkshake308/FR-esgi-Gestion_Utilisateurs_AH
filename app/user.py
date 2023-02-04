import random, hashlib

#  variable qui traque l'utilisateur actuellement connecté

current_user = None
def sha256_generator(str):
    m = hashlib.sha256()
    m.update(str.encode())

    return m.hexdigest()

def generate_login(p_nom, p_prenom):
    p_nom = p_nom.replace(" ", "")
    p_prenom = p_prenom.strip()
    return p_prenom[0]+p_nom

def generate_passwd():
    element = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-*/~$%&.:?!@"
    passwd = ""

    for i in range(9): passwd = passwd + element[random.randint(0, len(element) - 1)]
    passwd_hash = sha256_generator(passwd)
    return passwd

def user_add():
    nom = input("Entrez votre nom svp : ")
    prenom = input("Entrez votre prenom svp : ")
    passwd = generate_passwd()
    login = generate_login(nom, prenom)
    return nom, prenom, passwd, login
