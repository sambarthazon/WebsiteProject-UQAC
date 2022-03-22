# Flask application

Groupe : GRANES Johann, RIVET Victor, BARTHAZON Sam
Travail sur le dépôt Moodle de chacune des personnes du groupe


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
- https://getbootstrap.com/docs/4.0/components/navbar/

Vidéos :
- https://www.youtube.com/watch?v=dam0GPOAvVI : Tech With Tim
- https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH : Corey Schafer
- https://www.youtube.com/watch?v=OcD52lXq0e8 : FlaskCon


## Fonctionnement de l'application

Le premier admin doit être créé avec un username = 'Admin'. Ce dernier pourra par la suite promouvoir les utilisateurs qu'il voudra.


## Disfonctionnement de l'application

- Possibilité de créer une page d'erreur en éditant un user existant avec le username ou l'email d'un autre utilisateur existant.

- Un like et un commentaire d'un post seront conservé même lors de la suppression d'un post. Lorsque nous recréerons un post aillant le même post.id, il aura les likes et commentaires de l'ancien post.

- Un utilisateur connaissant les URL peut atteindre les pages qui ne lui sont autorisé comme par exemple avec la page de la liste des utilisateurs.
Nous avons néanmoins réussi à régler le problème avec la page de création de poste (URL: /post/create/public). Un lecteur rentrant cette URL aura un message comme quoi il n'a pas accés à cette page. Nous devons alors faire cette implémentation sur toutes les pages avec une redirection automatique de l'utilisateur.