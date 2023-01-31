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
def fetchdata_from_query(query):
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

def check_db():
    print("Vérification de l'existence de la base de données...", end=' ', flush=True)
    tables = fetchdata_from_query("SHOW TABLES;")
    if ("groups",) in tables:
        print('✔')
        time.sleep(1)
        return True
    else:
        print('❌')
        if not misc.prompt_yes_no("la base de donnée n'est pas créer souhaitez vous la créer maintenant ?"):
            print("L'application ne peut pas fonctionner sans base de donnée !")
            return False
    #  TO DO : create db
    try:
        sql = open("app/db_schema.sql", "r").read()
        fetchdata_from_query(sql)
    except Exception as e:
        print('Une erreur est survenue pendant la création de la base de données')
        print(e)
    return True

def bind_query():
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
