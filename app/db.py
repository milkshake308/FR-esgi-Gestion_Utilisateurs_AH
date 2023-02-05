import mysql.connector, time
from app import misc
from dotenv import dotenv_values
db_config = dotenv_values(".env")

dsn = {
    "host": db_config["db_host"],
    "port": db_config["db_port"],
    "user": db_config["db_user"],
    "password": db_config["db_pass"],
    "database": db_config["db_name"],
}
#  pre-generated query method
def direct_query(query):
    try:   
        with mysql.connector.connect(
            host=db_config["db_host"],
            user=db_config["db_user"],
            passwd=db_config["db_pass"],
            db=db_config["db_name"]
        ) as cnxn:
            with cnxn.cursor() as cursor:
                cursor.execute(query)
                r = cursor.fetchall()
                return r
    except Exception as e:
        print('❌')
        print(e)
        raise ConnectionError

#  parameters binding to query method
def bind_query(query: str, param = ()):
    try:   
        with mysql.connector.connect(
            host=db_config["db_host"],
            user=db_config["db_user"],
            passwd=db_config["db_pass"],
            db=db_config["db_name"]
        ) as cnxn:
            with cnxn.cursor() as cursor:
                # print('d',param)
                cursor.execute(query, param)
                
                r = cursor.fetchall()
                cnxn.commit()
                return r
    except Exception as e:
        print(e)

def check_db():
    print("Vérification de l'existence de la base de données...", end=' ', flush=True)
    tables = direct_query("SHOW TABLES;")
    if ("pf_users",) in tables:
        print('✔')
        time.sleep(1)
        return True
    else:
        print('❌')
        print("La base de donnée n'est pas crée !\nL'application ne peut pas fonctionner sans base de donnée !!")
        if not misc.prompt_yes_no("Voulez-vous réessayer la connexion ?"):
            return False
    return check_db()


