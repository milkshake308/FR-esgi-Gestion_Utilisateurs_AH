<!-----

Yay, no errors, warnings, or alerts!

Conversion time: 0.26 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β34
* Thu Jan 12 2023 04:38:19 GMT-0800 (PST)
* Source doc: Projet Semestre 1 - scripting python
* This is a partial selection. Check to make sure intra-doc links work.
----->


Projet Patient-First

<span style="text-decoration:underline;">Rappel du cahier des charges :</span>



* **Gestion des utilisateurs/administrateurs **: 
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

2. Installer les pré-requis avec : `pip install -r requirements.txt`

3. Créer la base de données patientfirst et assigner un utilisateur avec tout les droits dessus

4. Renseigner les informations nécéssaires pour la connexion a la base de données dans le env_example et renommer le fichier .env

<span style="text-decoration:underline;">Utilisation :</span>

1. Executer l'app avec `python main.py` 

