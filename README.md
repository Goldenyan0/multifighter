<div align="center">

# 🎮 Multifighter

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-000000?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-En%20développement-orange?style=for-the-badge)

*Jeu de combat 2D local – 1v1 sur le même clavier*

[![Rapport de projet](https://img.shields.io/badge/📄%20Rapport-Google%20Docs-blue?style=for-the-badge)](https://docs.google.com/document/d/1jaGiisIGufb-OoJfOKCOwXFJQ04h2jCh/edit?usp=sharing)

</div>

---

## 📌 Présentation

**Multifighter** est un jeu de combat **2D** développé en **Python** avec la bibliothèque **Pygame**.

Initialement inspiré de projets type *Bomberman* et *Archero*, le concept a évolué vers un **jeu de combat multijoueur local** en 1v1.

---

## 🎯 Concept

- ⚔️ Combat **1v1 en local** sur le même clavier
- Chaque joueur contrôle un personnage avec des capacités spécifiques
- **Objectif** : réduire la vie de l'adversaire à zéro
- Affichage d'un écran de **victoire** en fin de combat

---

## 🕹️ Fonctionnalités

### 🏠 Menu principal

| Bouton | Action |
|---|---|
| ▶️ JOUER | Lancer une partie |
| ⚙️ OPTIONS | Paramètres |
| ❌ QUITTER | Fermer le jeu |

### ⚔️ Système de jeu

- Sélection de personnages *(partiellement implémentée)*
- Combat en **temps réel**
- **Barre de vie** pour chaque joueur
- Système de **victoire**

### 🎮 Contrôles

> Clavier partagé entre les deux joueurs

| Action | Description |
|---|---|
| Déplacement | Touches directionnelles |
| Saut | Touche dédiée |
| Attaque | Touche dédiée |

---

## 🧰 Technologies utilisées

| Outil | Rôle |
|---|---|
| Python | Langage principal |
| Pygame | Moteur de jeu 2D |
| Photoshop 2020 | Création des assets graphiques |
| Visual Studio Code | Éditeur de code |

---

## 🧠 Choix techniques

- Utilisation de **Python** (langage maîtrisé)
- Appui sur des **tutoriels Pygame** pour les animations, hitbox et gestion de la vie
- Inspirations graphiques : *Street Fighter*, *Dragon Ball Z: Extreme Butōden*
- Travail avec **maquettes** et documents préparatoires

---

## 🧩 Architecture du projet

```
multifighter/
│── main.py          # Point d'entrée – menu principal
│── button.py        # Classe Button – interactions UI
│── fighter.py       # Classe Fighter – logique des personnages
│── assets/
│   ├── images/      # Sprites et animations
│   ├── audio/       # Musiques et effets sonores
│   └── backgrounds/ # Fonds de scène
```

### 🔧 Classe `Button`

| Méthode | Rôle |
|---|---|
| `__init__()` | Initialisation du bouton |
| `update()` | Affichage |
| `checkForInput()` | Détection du clic |
| `changeColor()` | Effet hover |

### 🥊 Classe `Fighter`

**Attributs principaux :**

| Attribut | Description |
|---|---|
| `x, y` | Position du personnage |
| `joueur` | Joueur 1 ou 2 |
| `animations` | Frames d'animation |
| `état` | Attaque, mouvement, idle… |

**Méthodes :**

| Méthode | Rôle |
|---|---|
| `load_images()` | Chargement des animations |
| `move()` | Gestion des déplacements |
| `attack()` | Gestion des attaques |
| `update()` | Mise à jour globale |

---

## ▶️ Installation & Lancement

**1. Installer la dépendance**

```bash
pip install pygame
```

**2. Cloner le projet**

```bash
git clone https://github.com/Goldenyan0/multifighter.git
cd multifighter
```

**3. Lancer le jeu**

```bash
python main.py
```

---

## ⚠️ Difficultés rencontrées

| Problème | Détail |
|---|---|
| Transition menu → jeu | Non fonctionnelle |
| Gestion du son | Problèmes d'intégration |
| Fonds animés (GIFs) | Incompatibilité Pygame |
| Animations | Temps de création élevé |
| Sélection de personnage | Non finalisée |

---

## 🚀 Améliorations possibles

- [ ] Finaliser la sélection de personnages
- [ ] Corriger la transition menu → jeu
- [ ] Ajouter des attaques spéciales
- [ ] Effets visuels avancés
- [ ] Menu options fonctionnel *(résolution, musique, thème)*
- [ ] Amélioration des graphismes et de l'ergonomie

---

## 📊 Bilan

> Ce projet a permis d'approfondir les compétences en **Python** et **Pygame**, de comprendre les contraintes réelles d'un projet de jeu vidéo et d'améliorer le travail en équipe.
>
> Malgré des limites techniques, le jeu est **fonctionnel dans ses bases** et constitue une solide base d'évolution.

---

## 📚 Sources

| Ressource | Lien |
|---|---|
| Sprites & animations | [spritedatabase.net](https://spritedatabase.net/) |
| Éditeur de code | [Visual Studio Code](https://code.visualstudio.com/) |
| Musiques | [YouTube](https://www.youtube.com/) |

> ✅ Toutes les ressources utilisées sont **libres de droits**.

---

<div align="center">
  <i>Projet scolaire – Jeu de combat 2D local</i><br/>
  <i>Python · Pygame · Photoshop</i>
</div>
