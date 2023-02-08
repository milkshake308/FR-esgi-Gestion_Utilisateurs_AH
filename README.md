
Projet Patient-First

<span style="text-decoration:underline;">Rappel du cahier des charges :</span>



* **Gestion des utilisateurs/administrateurs**: 
    *  Créer de nouveaux Utilisateurs selon les profils et les droits définis. 
    *  Définir les règles de gestion et de sécurité des login/pwd (Login : contraction de la première lettre du prénom et du nom utilisateur (non composé), (PWD : génération aléatoire et hachage avant sauvegarde persistante, durée de validité, ...) 
    * Modifier/supprimer un utilisateur/un admin.
    * Consulter la liste des utilisateurs/des admins. 
    * Rechercher un utilisateur/un admin particulier. 
    * Stocker les données dans un dictionnaire ou dans un fichier CSV ou dans une base de données. 
    * Permettre les accès aux divers admins et corps de métier (pas les patients) via une authentification contrôlée.

<span style="text-decoration:underline;">Fonctionnalités à produire :</span>

* Stockage dans base de données
* Règles de gestion et sécurisation des logins :
    * génération mot de passe prédéfini aléatoirement
    * niveau de privilège
    * génération d’un login prédéfini
    * hachage de mot de passe
* Ajout/modification/suppression des utilisateurs/admins
* Consultation/Recherche des utilisateurs/admins
* Gestion des accès via une authentification contrôlée

<span style="text-decoration:underline;">Installation :</span>

1. Récupérer le projet `git clone https://github.com/milkshake308/Gestion_Utilisateurs_AH.git`

2. Aller dans le dossier du projet et installer les pré-requis avec : `pip install -r requirements.txt`

3. Créer la base de données patientfirst et assigner un utilisateur avec tout les droits dessus
* Exemple avec docker : 
    * Créer le conteneur de base de données : 
    ` docker run --name pfadb0 -e MYSQL_ROOT_PASSWORD=3srcc2023 -e MYSQL_USER=pfa -e MYSQL_PASSWORD=pfaadm -e MYSQL_DATABASE=pfa -p 3306:3306 -d mariadb `                     
    * Charger la base de données : 
    ` docker exec -i pfadb0 mysql -uroot -p3srcc2023 pfa < app/db_schema.sql `                     

4. Renseigner les informations nécéssaires pour la connexion a la base de données dans le env_example et renommer le fichier .env

<span style="text-decoration:underline;">Utilisation :</span>

1. Executer l'app avec `python main.py`
2. Vous pouvez saisir les identifiants `admin admin` par défaut pour vous connecter

