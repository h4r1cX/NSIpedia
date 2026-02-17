# Cours sur les Graphes
[retour à l'accueil](https://github.com/h4r1cX/NSIpedia/blob/main/accueil.md)

## C'est quoi un graphe ?
Ce sont des sommets reliés par des arétes

## Types de graphes :
- Connexe : N'importe quelle paire de sommets est reliable par un chemin (suite finie d'arrets) dans le graphe
- Orientée : ...
- Ponderer : ...

## Matrice d'adjacence :
C'est un tableau de nombre.
Représentation en python : 
```py
   M_g = [
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            ...
        ] 
```
M_g[i][j] = 1 si arète de Si ver Sj. Sinon = 0