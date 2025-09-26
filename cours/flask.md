# 📁 Flask
[retour à l'accueil](https://github.com/h4r1cX/NSIpedia/blob/main/accueil.md)
---


## Qu’est-ce que Flask ?
- **Flask** est un micro-framework Python qui permet de créer des applications web.  
- Flask s'occupe de lier le code Python avec le code HTML/CSS

## Installation
```bash
pip install flask
```

## Premier serveur Flask
```python
from flask import Flask

# création de l’application
app = Flask(__name__)

# route racine
@app.route("/")
def accueil():
    return "Bonjour, Flask !"

# lancer le serveur
if __name__ == "__main__":
    app.run(debug=True)
```

## Explications :
- `Flask(__name__)` : crée l’application.  
- `@app.route("/")` : définit une **route** (URL).  
- `app.run(debug=True)` : lance le serveur en mode debug (rechargement automatique + erreurs détaillées).  

## Route simple
```python
@app.route("/hello")
def hello():
    return "Salut à toi !"
```

👉 Accessible sur : `http://127.0.0.1:5000/hello`

## Paramètres dans l’URL
```python
@app.route("/user/<nom>")
def bonjour_user(nom):
    return f"Bonjour {nom} !"
```
👉 Exemple : `http://127.0.0.1:5000/user/Alice` ➝ `Bonjour Alice !`

## Méthodes HTTP (GET et POST)
```python
from flask import request

@app.route("/formulaire", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        nom = request.form["nom"]
        return f"Formulaire reçu : {nom}"
    return '''
        <form method="POST">
            Nom : <input type="text" name="nom">
            <input type="submit" value="Envoyer">
        </form>
    '''
```

👉 Ici :  
- **GET** : affiche le formulaire.  
- **POST** : récupère la donnée envoyée.  

## Templates HTML avec Jinja2
Flask utilise **Jinja2** pour séparer le code Python du HTML.  
Créer un fichier `templates/index.html` :

```html
<!DOCTYPE html>
<html>
<head>
    <title>Accueil Flask</title>
</head>
<body>
    <h1>Bonjour {{ nom }}</h1>
</body>
</html>
```

Et dans `app.py` :
```python
from flask import render_template

@app.route("/template/<nom>")
def template(nom):
    return render_template("index.html", nom=nom)
```

👉 Résultat : l’HTML s’affiche avec le nom injecté.  