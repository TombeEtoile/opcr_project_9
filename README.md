# OPCR P9 LitReviews

## Installation & Lancement

### Prérequis

Commencez tout d'abord par installer [Python 3.10](https://www.python.org/downloads/release/python-3100/).

### Installation

1. Lancez la console et placez-vous dans le dossier de votre choix, puis clonez ce repository :

    ```bash
    git clone https://github.com/TombeEtoile/opcr_project_9.git
    ```

2. Placez-vous dans le dossier cloné :

    ```bash
    cd opcr_project_9
    ```

3. Créez un nouvel environnement virtuel :

    ```bash
    python -m venv env
    ```

4. Activez l'environnement virtuel :

    - Sur Windows :

      ```bash
      env\scripts\activate.bat
      ```

    - Sur Linux :

      ```bash
      source env/bin/activate
      ```

5. Installez les packages requis :

    ```bash
    pip install -r requirements.txt
    ```

### Configuration de la base de données

1. Placez-vous à la racine du projet (là où se trouve le fichier `manage.py`), puis effectuez les migrations :

    ```bash
    python manage.py makemigrations
    ```

2. Appliquez les migrations :

    ```bash
    python manage.py migrate
    ```

### Lancement du serveur

1. Lancez le serveur de développement :

    ```bash
    python manage.py runserver
    ```

2. Vous pouvez ensuite utiliser l'application à l'adresse suivante :

    [http://127.0.0.1:8000](http://127.0.0.1:8000)
