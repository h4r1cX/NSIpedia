# Cours sur les Piles
[retour à l'accueil](https://github.com/h4r1cX/NSIpedia/blob/main/accueil.md)

## Notation Polonaise inversée (NPI) :
- 3 + 5 --> +_3_5
- 7 - (3 + 9) --> -_7_+_3_9
- 7 - ((3 + 9) - 7) --> -_7_-_+_3_9_7

## Class
* class File :
  ```python
  class File:
    def __init__(self, t):
        self.__taille = t
        self.__data = [None] * self.__taille
        self.__s = 0
        self.__e = 0

    def estVide(self):
        return self.__s == self.__e
    
    def est_pleine(self):
        return self.__e - self.__s == self.__taille 

    def enfiler(self, x):
        if self.est_pleine():
            raise Exception('File pleine')
        else:
            self.__data[self.__e % self.__taille] = x
            self.__e += 1

    def defiler(self):
        if self.est_vide():
            raise Exception("Pile vide")
        else:
            x = self.__data[self.__s % self.__taille]
            self.__s += 1
            return x
        
    def __repr__(self):
        res = []
        for i in range(self.__s, self.__e):
            res.append(self.__data[i % self.__taille])
        return str(res)

---

## Implémenter les Files :
```shell
    >>> from collections import deque
    >>> f = deque([])
    >>> f.append(7)
    >>> f
    deque([7])
    >>> f.append(3)
    >>> f.popleft()
    7
    >>> x = f.popleft()
    >>> x
    3
```