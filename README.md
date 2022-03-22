# Flask application

Groupe : GRANES Johann, RIVET Victor, BARTHAZON Sam


## Conditions préalables:

Vous devez avoir déjà installé :
- python
- pip
- virtualenv


## Mise en place du projet

1. Décompressez le fichier
2. Allez dans le dossier du projet et installez un dossier d'environnement virtuel : 
```
virtualenv .venv
```


3. Activez l'environnement virtuel :
```
source .venv/bin/activate (linux)
```
```
.venv\Scripts\activate.bat (windows)
```


4. Installez toutes les bibliothèques et extensions requises pour ce projet. Toutes les dépendances sont répertoriées dans le fichier requirements.txt. Exécutez la commande ci-dessous pour les installer tous en une seule commande (windows ou linux) :
```
pip install -r requirements.txt
```


## Sources qui ont aidé au développement

Sites :
- https://flask.palletsprojects.com/en/2.0.x/tutorial/
- https://flask.palletsprojects.com/en/2.0.x/testing/
- https://flask.palletsprojects.com/en/2.0.x/tutorial/tests/

Vidéos :
- https://www.youtube.com/watch?v=dam0GPOAvVI : Tech With Tim
- https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH : Corey Schafer
- https://www.youtube.com/watch?v=OcD52lXq0e8 : FlaskCon


## Fonctionnement de l'application

Le premier admin doit être créé avec un username = 'Admin'. Ce dernier pourra par la suite promouvoir les utilisateurs qu'il voudra.

Un like et un commentaire d'un post seront conservé même lors de la suppression d'un post. Lorsque nous recréerons un post aillant le même post.id, il aura les likes et commentaires de l'ancien post.


## Disfonctionnement de l'application

Possibilité de créer une page d'erreur en étant sur le compte de l'admin (donc l'utilisateur avec le username 'Admin') et edit un user existant avec le username ou l'email d'un utilisateur existant.