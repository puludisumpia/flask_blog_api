# CREATION D'UNE API REST AVEC FLASK ET SQLALCHemy

Bonjour, je vous montre via cette application comment realisé une api rest avec [Flask](https://flask.palletsprojects.com) et [sqlalchemy](https://docs.sqlalchemy.org). 

Python est un langage de Pragrammation disposant d'une syntaxe simple et claire, j'espère vous n'aurez pas beaucoup de difficultés à comprendre la logique de conception de cette api.

## Obtenir cette application


Cette application est libre de droit et entièrement gratuite, vous pouvez bien l'intégrer dans vos projects Flask.
Alors, il suffit juste de cloner le repository, en faisant:

**<code>git clone https://github.com/puludisumpia/flask_blog_api.git</code>**

Entrer dans le dossier en faisant **<code> cd flask_blog_api </code>**

Ensuite créez un environnement virtuel, je rappelle que ça se fait via la commande: **<code>python3 -m venv nom_virtual_env</code>**. Il faut bien sûr l'activer **<code>source nom_virtual_env/bin/activate</code>**.

Installer les packets: **<code>pip3 install requirements.text</code>**

Normalement si toutes les étapes sont respectées, tout devrait marcher  **nice**

## Vocabilaire HTTP (Facultatif)

Vous pouvez utiliser **curl** pour tester toutes les méthodes http.
Exemple: <code>curl http://127.0.0.1:5000/posts/</code>.

Voici les méthodes les plus utilisées:
1. **GET**: C'est la méthode la plus courante pour demander une ressource. Une requête GET est sans effet sur la ressource, il doit être possible de répéter la requête sans effet.
2. **POST**: Cette méthode est utilisée pour transmettre des données en vue d'un traitement à une ressource. L'URI fourni est l'URI d'une ressource à laquelle s'appliqueront les données envoyées.
3. **PATCH**:Cette méthode permet, contrairement à PUT, de faire une modification partielle d'une ressource.
4. **DELETE**:Cette méthode permet de supprimer une ressource du serveur.


## Apropos de l'auteur

Je suis un passionné de la programmation informatique. J'aime coder avec Python, je prône l'évangélisation de Django et Falsk. 

Cette api a été pensée et codée par Mpia M.


