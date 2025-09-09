# FIRST COMMIT !!!
Installer git sur votre ordinateur => https://git-scm.com/

Ensuite, vous faites :
git --version          # pour vérifier que Git est bien installé

# INITIALISATION
git init               # initialise le projet Git en local
git add .              # ajoute tous les fichiers au suivi
git commit -m "message" # premier commit
git remote add origin https://github.com/h4r1cX/NSIpedia.git # lier le dépôt local au dépôt GitHub
git branch -M main     # renommer la branche en "main"
git push -u origin main # envoyer sur GitHub

# ET APRES TOUT CA ?
git status             # voir les fichiers modifiés ou en attente

# VOS COMMITS (cycle classique)
git pull               # mettre à jour avant de bosser (récupérer les changements de GitHub)
git add .              # ajouter les changements
git commit -m "message" # enregistrer les changements
git push               # envoyer sur GitHub
