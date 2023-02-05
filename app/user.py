import getpass,os, app.db as db, app.misc as misc


#  Vérification de l'existence de l'utilisateur par défaut

def check_default():
    try:
        val = db.direct_query("SELECT * FROM pf_users where login = 'admin'")
        if val : print("Configuration OK !")
        else : print("Impossible de trouver l'utilisateur par défaut, essayer de reconstruire la base de donnée")
    except Exception as e:
        print(e)

def user_add():
    nom = input("Entrez votre nom svp : ")
    prenom = input("Entrez votre prenom svp : ")
    passwd, passwd_hash = misc.generate_passwd()
    login = misc.generate_login(nom, prenom)
    #  Vérifie si le login existe déja
    if db.bind_query("SELECT * FROM pf_users WHERE login = %s", (login,)) :
        if misc.prompt_yes_no("Un utilisateur existe déja pour l'identifiant {}, souhaitez-vous en creér un autre ?".format(login)):
            return user_add()
        else:
            return

    print("Voici le nom de l'utilisteur :", login,"\nVoici le mot de passe utilisateur",passwd,"\nAttention vous ne pourrez plus reconsulter son mot de passe !!")
    #  Ajoute l'utilisateur 
    new_user = (prenom, nom, login, passwd_hash)
    db.bind_query("INSERT INTO pf_users(user_firstname, user_lastname, login, hashed_password) VALUES (%s, %s, %s, %s)", new_user)

    #  Ajoute l'utilisateur au groupe pf_users par défaut
    r = db.bind_query("SELECT user_id FROM pf_users WHERE login = %s", (login,))
    db.bind_query("INSERT INTO pf_user_membership(group_id, user_id) VALUES (2, %s)", r[0])
    input("Appuyer sur un touche pour continuer...")


def user_login():
    login = input('Login :')
    password = getpass.getpass('Password :')
    query = """
    SELECT u.user_id, u.user_firstname, u.user_lastname, g.group_name, u.password_timestamp
    FROM pf_users u 
    JOIN pf_user_membership um ON um.user_id = u.user_id
    JOIN pf_groups g ON g.group_id = um.group_id
    WHERE login = %s and hashed_password = %s;
    """
    r = db.bind_query(query, (login, misc.sha256_generator(password)))
    if r:
        r = list(r[0])
        time_format = "%Y-%m-%d %H:%M:%S"
        return {
            'user_id': r[0],
            'firstname': r[1],
            'lastname': r[2],
            'group_name': r[3],
            'password_update': r[4]
        }
    else:
        print("Identifiant ou mot de passe incorrect !!")
        return user_login()

def search_user():
    r = input("Premières lettres du nom ou prenom de l'utilisateur recherché (Laissez vide pour tout les utilisateurs) :")
    r = r + '%'
    query = """
    SELECT CONCAT(user_firstname,' - ', user_lastname) FROM pf_users WHERE user_lastname LIKE %s OR user_firstname LIKE %s;
    """
    r = db.bind_query(query, (r,r))
    if r :
        print("Voici les utilisateurs trouvés : ") 
        print([user[0] for user in r])  
    else:
        print("Aucun utilisateur trouvé !")

    if misc.prompt_yes_no('Voulez faire une nouvelle recherche ?'):
        os.system("clear")
        return search_user()

def change_passwd(user_id):
    if misc.prompt_yes_no('Voulez-vous obtenir un mot de passe pré-généré ?'):
        new_passwd, new_hashed_passwd = misc.generate_passwd()
        print('Votre nouveau mot de passe est :', new_passwd)
    else:
        new_passwd = getpass.getpass("Nouveau mot de passe :")
        new_hashed_passwd = misc.sha256_generator(new_passwd)
    query = """
    UPDATE pf_users SET hashed_password = %s WHERE user_id = %s;
    """
    db.bind_query(query,(new_hashed_passwd,user_id))
