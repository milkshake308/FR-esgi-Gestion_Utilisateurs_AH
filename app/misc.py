import random, hashlib

# Variable toggle d'éxécution
app = True


def prompt_yes_no(prompt: str):
    while True:
        response = input((prompt+' [o/N]: '))
        if response.lower() in ["y", "yes", "o", "oui"]:
            return True
        elif response.lower() in ["n", "no", "non"]:
            return False
        else:
            print("Merci de saisir 'oui' ou 'non'.")
            return prompt_yes_no(prompt)


def sha256_generator(str):
    m = hashlib.sha256()
    m.update(str.encode())

    return m.hexdigest()

def generate_login(p_nom, p_prenom):
    p_nom = p_nom.replace(" ", "")
    p_prenom = p_prenom.strip()
    return str(p_prenom[0]+p_nom)

def generate_passwd():
    element = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-*$&!@"
    passwd = ""

    for i in range(9): passwd = passwd + element[random.randint(0, len(element) - 1)]
    passwd_hash = sha256_generator(passwd)
    return passwd, passwd_hash
