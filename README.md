🎮 Multifighter

📌 Présentation du projet

Multifighter est un jeu de combat en 2D développé en Python avec la bibliothèque Pygame.

Initialement, plusieurs idées ont été envisagées (inspirations type Bomberman et Archero), avant de converger vers un jeu de combat multijoueur local.

🎯 Concept
Jeu 1v1 en local (même clavier)
Chaque joueur contrôle un personnage avec des capacités spécifiques
Objectif : faire tomber ou éliminer l’adversaire
Affichage du résultat avec un système de victoire
🕹️ Fonctionnalités
Menu principal
Bouton JOUER
Bouton OPTIONS
Bouton QUITTER
Système de jeu
Sélection de personnages (partiellement implémentée)
Combat en temps réel
Barre de vie
Système de victoire
Contrôles
Clavier partagé (touches directionnelles + attaques + saut)
⚙️ Technologies utilisées
Python
Pygame
Photoshop 2020 (assets graphiques)
Visual Studio Code
🧠 Choix stratégiques
Utilisation de Python (langage maîtrisé)
Appui sur des tutoriels Pygame pour :
animations
hitbox
gestion de la vie
Inspirations graphiques :
Street Fighter
Dragon Ball Z: Extreme Butōden
Travail avec maquettes et documents préparatoires
⚔️ Système de combat
Combat entre 2 joueurs
Actions possibles :
se déplacer
sauter
attaquer
Objectif :
réduire la vie adverse à 0
Résultat :
affichage "Victoire"
🧩 Architecture du projet
Menu
main.py
gestion du menu principal
affichage
navigation
button.py
classe Button
gestion des interactions
Classe Button
__init__ → initialisation
update() → affichage
checkForInput() → détection clic
changeColor() → effet hover
Jeu
Classe Fighter

Représente un personnage jouable.

Attributs principaux :

position (x, y)
joueur (1 ou 2)
animations
état (attaque, mouvement…)

Méthodes :

load_images() → chargement des animations
move() → gestion des déplacements
attack() → gestion des attaques
update() → mise à jour globale
⚠️ Difficultés rencontrées
Transition menu → jeu non fonctionnelle
Problèmes avec :
le son
les GIFs en fond
Temps élevé pour :
animations
création des personnages
Sélection de personnage non finalisée
🚀 Améliorations envisagées
Finaliser :
menu de sélection des personnages
transition menu → jeu
Ajouter :
attaques spéciales
effets visuels avancés
Implémenter options :
résolution
musique
thème
Améliorer :
ergonomie
graphismes
📊 Bilan

Le projet a permis :

d’améliorer le travail en équipe
d’approfondir les compétences en Python et Pygame
de comprendre les contraintes réelles d’un projet

Malgré des limites techniques, le jeu est fonctionnel dans ses bases et constitue une bonne base d’évolution.

📚 Sources
Animations : https://spritedatabase.net/
Éditeur de code : https://code.visualstudio.com/
Musiques : https://www.youtube.com/

Les ressources utilisées sont libres de droits.

▶️ Lancer le projet
pip install pygame
python main.py
