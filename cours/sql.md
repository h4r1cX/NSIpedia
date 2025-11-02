# 📁 SQL
[retour à l'accueil](https://github.com/h4r1cX/NSIpedia/blob/main/accueil.md)
---

## Vocabulaire :
- Clé primaire : Une ou plusieurs colonnes telles que aucune ligne n'a les même valeurs dans cette(ces) colonnes(s). Un moyen d'identifier de manière unique chaque ligne dans la table

- Clé étrangère : Champ qui fait référence à une clé primaire d'une autre table
   ```sql
   foreing key

- Cohérance : Impossible INSERT lignes dans table fille avec une valeur de clé étrangère n'existant pas dans la table mère.

- SQL : Structured Query Language

- SGBD : Système de Gestion de Base de Données

## Forme normales :

* Formes que nous utilisons en cours :
- 0NF : Non redendance (pas de répétition de lignes des tables)
- 1NF : Atomicité : une seule valeur par cellule.
- 2FN : Si la table a une clé primaire composée (plusieurs colonnes) alors aucune colonne non clé ne doit dépendre seulement d'une partie de cette clé (elle doit dépendre de toute la clé). Pas de dépendance partielle (Clé primaire composite, colonne dépendante que d'une partie de la clé) 
- 3NF :  Toute les colones dépendents directement de la clé primaire. Une colonne ne doit pas dépendre d'une autre colonne non clé (pas de dépendance transitive)

## Tables

* Crée : 
   ```sql
   CREATE TABLE nom(shéma);

* Lire : 
   ```sql
   DROP TABLE nom;

* Ajouter : 
   ```sql
   INSERT INTO table VALUES(v1, v2, ...);

* Suprimer : 
   ```sql
   DELETE FROM table WHERE c = v;

* Mettre a jour :
   ```sql
   UPDATE table SET c = v WHERE x = z;
Remplace par 'v' la valeur du champ 'c' de l'enregistrement de la table où la valeur de 'x' est 'z'.

* Selectionner :
   ```sql
    SELECT c2, c4 
    FROM table 
    WHERE c1 = 5;

* Jointure entre deux tables:
   ```sql
    SELECT club.nom, joueur.id_nom -- Nous ne somme pas obligé de mettre le nom de la table avant
    FROM joueur
    JOIN club
    ON joueur.id_club = club.id_club;
