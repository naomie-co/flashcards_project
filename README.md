# OC projet 13 – Flashcards project

## Le projet
Le site Flashcards project a pour objectif de faciliter l’apprentissage par la création de cartes et la consultation régulière de celles-ci 

## Le parcours utilisateur 
Dans cette V.1 du projet, l’utilisateur peut créer des flashcards après s’être connecté à un compte, via la barre de navigation. Les cartes créées sont rattachées à un paquet thématique, prédéfini. 

L’utilisateur peut consulter les cartes rattachées à un paquet à partir de la page d’accueil :
-	La première question s’affiche
-	Après avoir cliqué sur le bouton « afficher la réponse », celle-ci apparait ainsi que les boutons d’auto-évaluation (OK, MEH ou NOK). 
-	L’autoévaluation est sauvegardée dans l’historique de l’utilisateur. 
-	Possibilité de passer à la carte suivante via un bouton de pagination. 
L’historique est accessible à partir de la barre de navigation et permet d’afficher un tableau avec la liste des cartes affichées. 

## Pour installer le projet en local

### 1 – Création de l’environnement virtuel
Cloner ce repo

Ce programme est exécuté en Python et utilise le Framework Django.

Pour l’exécuter, il est recommandé de créer au préalable, un environnement virtuel.

Une fois l’environnement virtuel créé, lancez l’installation des dépendances avec la commande :

	pip install -r requirements.txt

### 2 – Créer la base de données 
Le projet utilise une base de données SQLite en local

La base de données doit être déclarée dans le projet Django dans le fichier settings.py.

### 3 – Lancer l’initialisation de la base de données
Pour installer la base de données dans l'environnement virtuel lancez la commande suivante :

	manage.py makemigrations

	manage.py migrate

### 4 – Lancer le serveur
Pour accéder à la plateforme, lancez le serveur Django avec la commande suivante :
	
	manage.py runserver

Ajoutez l’adresse donnée par le serveur dans un navigateur.

### Vérification PEP 8 et informations sur les tests
Si vous souhaitez lancer les vérifications de conformité à la PEP 8 sans les erreurs liées à Django :
-	Installez dans l’environnement virtuel :
	
		pip install pylint-django
	
-	Lancez la commande
	
		pylint test file.py --load-plugins=pylint_django


Le fichier de tests de l’application cards comprend des tests fonctionnels qui utilisent Selenium.

Pour installer Selenium dans le projet, exécutez la commande suivante :

	pip install selenium

Installez le driver correspondant au navigateur Firefox (https://github.com/mozilla/geckodriver/releases).

Remplacez le lien vers geckodriver dans le fichier de tests par le vôtre.

## Lien vers le site
Si vous souhaitez tester le site flashcards_project, cliquez sur ce lien : [http://flashcards-project13.herokuapp.com/]




