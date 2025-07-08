<div style="margin-bottom: 0.1em;">
<span style="color: darkorange;">Création du dépôt Git</span><br>
1. Aller sur ***https://github.com/dashboard*** et créer votre nouveau
repository nommé ApprendreDjango<br>
2. Ouvrer l'invite de commande à la racine de votre projet Django
nommé ApprendreDjango
</div>

```bash
git init
git add .
git commit -m "Création de notre projet Django ApprendreDjango"
git branch -M main
git remote add origin https://github.com/ben2ci/ApprendreDjango.git
git push -u origin main
```

<div style="color: darkorange; margin-bottom: 0.1em;">
Récupérer le dépôt distant
</div>

```bash
git clone https://github.com/ben2ci/ApprendreDjango.git
cd ApprendreDjango
```

<div style="color: darkorange; margin-bottom: 0.1em;">
Après toute modification du projet
</div>

```bash
git status
git add .
git commit -m "Modifications apportées au projet"
git branch -M main
git pull -u origin main
git push -u origin main
```

<div style="color: darkorange; margin-bottom: 0.1em;">
Lancer le Projet
</div>

```bash
python manage.py runserver localhost:9000
```

<div style="color: darkorange; margin-bottom: 0.1em;">
Mise à jour de PIP
</div>

```bash
python.exe -m pip install --upgrade pip
```
<div style="color: darkorange; margin-bottom: 0.1em;">
Enregistrer les packages installés
</div>

```bash
pip freeze > requirements.txt
```

<div style="color: darkorange; margin-bottom: 0.1em;">
Installer les dépendances du projet
</div>

```bash
pip install -r requirements.txt
```

<div style="color: darkorange; margin-bottom: 0.1em;">
Créer ou applique les changements à la base de données
</div>

```bash
python manage.py migrate
```
<div style="color: darkorange; margin-bottom: 0.1em;">
Appliquer les changements pour la base de données
</div>

```bash
python manage.py makemigrations
```

<div style="color: darkorange; margin-bottom: 0.1em;">
Lancer le shell Django
</div>

```bash
.venv\Scripts\activate
python manage.py shell
```

<div style="color: forestgreen; margin-bottom: 0.1em;">
Commandes :
</div>

```bash
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()

>>> from django.conf import settings
>>> settings.SECRET_KEY
>>> settings.BASE_DIR
```

<div style="color: darkorange; margin-bottom: 0.1em;">
Commande après l'installation de MySQL
</div>

```bash
(.venv) mysql -u ghostyrex -p
Enter password: rootMysql@2210
(mysql> create database restaurant_db;)
mysql> show databases;
mysql> use restaurant_db;
mysql> show tables;
```