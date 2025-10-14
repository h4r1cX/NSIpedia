# 📁 SQL
[retour à l'accueil](https://github.com/h4r1cX/NSIpedia/blob/main/accueil.md)
---

## Vocabulaire :
- Clé primaire : Une ou plusieurs colonnes telles que aucune ligne n'a les m valeurs dans cette(ces) colonnes(s). Un moyen d'identifier de manière unique chaque ligne dans la table

## Forme normales :

* Formes que nous utilisons en cours :
- 0NF : Non redendance (pas de répétition de lignes des tables)
- 1NF : Atomicité : une seule valeur par cellule.
- 2FN : Pas de dépendance partielle (Clé primaire composite, colonne dépendante que d'une partie de la clé)
- 3FN : Pas de dépendance transitive

## Tables

* Crée : 
CREATE TABLE nom(shéma);

* Lire : 
DROP TABLE nom;

* Ajouter : 
INSERT INTO table VALUES(v1, v2, ...);

* Suprimer : 
DELETE FROM table WHERE c = v;

* Mettre a jour : UPDATE table SET c = v WHERE x = z;
Remplace par 'v' la valeur du champ 'c' de l'enregistrement de la table où la valeur de 'x' est 'z'.

* Selectionner :
SELECT c2, c4 
FROM table 
WHERE c1 = 5;

* Jointure entre deux tables:
SELECT club.nom, joueur.id_nom -- Nous ne somme pas obligé de mettre le nom de la table avant
FROM joueur
JOIN club
ON joueur.id_club = club.id_club;
