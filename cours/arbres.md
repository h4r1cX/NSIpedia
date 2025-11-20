## Cours sur les arbres. 

1. Qu'est-ce qu'un arbre? 
-> Un arbre est une structure de données créer pour organiser des valeurs d'une listes.

2. De quoi un arbre est-il composé? 
-> l'abre est composé d'une première valeur appelée racine et de deux sous arbres, un à gauche et un à droite. Les deux premières valeurs de ces deux sous arbres vont à leur tour devenir les racines de leurs arbres respectifs. 

3. Comment créer un arbre? 
-> Tout d'abord, il faut importer les annotations. Pour cela, il faut faire:

```
from __future__ import annotations
```

-> Pour ensuite créer un arbre, il faut instencier des valeurs. Voici un exemple:

```
a1 = (8,
     (2,(),()),
     (1,
       (15, (), 5)))
```

4. Quelques fonctions pour aider à se repérer dans un arbre. 

```
def empty(a):
    return a == ()

def racine(arbre):
    if empty(arbre):
        return None
    else:
        return arbre[0]
    
def gauche(arbre):
    if empty(arbre):
        return ()
    else:
        return arbre[1]

def droite(arbre):
    if empty(arbre):
        return ()
    else:
        return arbre[2]

def est_dans(x, a):
    """
    renvoie True si x est dans a
    False sinon
    """
    if empty(a):
        return False #l'arbre vide ne contient aucune valeur
    else:
        return x == racine(a) or est_dans(x, gauche(a)) or est_dans(x, droite(a))


def taille(a):
    if empty(a):
        return 0
    else :
        return 1 + taille(gauche(a)) + taille(droite(a))
```
