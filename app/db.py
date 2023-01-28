import mysql.connector
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
        with mysql.connector.connect(**dsn) as cnxn:
            with cnxn.cursor() as cursor:
                cursor.execute(query)
                r = cursor.fetchall()
                return r
    except:
        raise ConnectionError

def check_db():
    tables = fetchdata_from_query("SHOW TABLES")
    if ("groups",) in tables:
        return True
    else:
        if not misc.prompt_yes_no("la base de donnée n'est pas créer souhaitez vous la créer maintenant ?"):
            print("L'application ne peut pas fonctionner sans base de donnée !")
            global app
            app = False
            return
    #  TO DO : create db
    sql = open("db_schema.sql", "r")
    fetchdata_from_query(sql)

