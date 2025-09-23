# 📁 STRUCTURES DE DONNES
---

## Liste python :
`li = [7,1,9,"a"]`
* lire :
  ```python
  >>> li[2]
   9
* écrire :
  ```python
  li[3] = 12
  >>> print(li)
  [7, 1, 12, "a"]

* append ajoute un élément à la fin de la liste. :
  ```python
  >>> li = [7, 1, 9, "a"]
  >>> li.append("banane")   # ajoute str "banane" à la fin
  >>> print(li)
  [7, 1, 9, "a", "banane"]

* enlever le dernier élément d'une liste (système de piles)
  ```python
  >>> li = [7, 1, 9]
  >>> a = li.pop()
  >>> print(li)
  [7, 1]
  >>> print(a)
  9

## Dictionaire :
`dico = {"a" : 1, "b" : 2, "c" : 14}`
* lire : 
  ```python
  >>>dico["a"]
  1

* écrire :
  ```python
  >>>dico["a"] = 2025
  >>>print(dico)
  {"a" : 2025, "b" : 2, "c" : 14}

* ajout d'un élément à la fin du dictionaire. :
  ```python
  >>> dico["d"] = 0
  >>> print(dico)
  {"a" : 2025, "b" : 2, "c" : 14, "d" : 0}