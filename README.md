# FrozenLake-QLearning
Parfait ! Pour un projet **FrozenLake-QLearning**, ton `README.md` doit être **clair, structuré et informatif**, pour que quelqu’un d’autre comprenne ton projet, puisse l’installer et l’utiliser facilement. Voici une structure complète que tu peux suivre :

---

# FrozenLake-QLearning

Projet pédagogique d’apprentissage par renforcement utilisant **Q-learning** sur l’environnement **FrozenLake** de Gymnasium. L’agent apprend à naviguer sur une grille pour atteindre l’objectif tout en évitant les trous.

---

## Table des matières

1. [Description](#description)
2. [Structure du projet](#structure-du-projet)
3. [Installation](#installation)
4. [Utilisation](#utilisation)
5. [Scripts principaux](#scripts-principaux)
6. [Visualisation](#visualisation)
7. [Licence](#licence)

---

## Description

Ce projet implémente un **agent intelligent** capable d’apprendre la meilleure politique pour naviguer dans l’environnement FrozenLake.

* Algorithme utilisé : **Q-learning**.
* Objectif : Atteindre la case but (`G`) en évitant les trous (`H`).
* Environnement : `gymnasium.make("FrozenLake-v1")`.


---

## Installation

1. Cloner le dépôt :

```bash
git clone https://github.com/islemfatnassi/FrozenLake-QLearning.git
cd FrozenLake-QLearning
```

2. Créer un environnement virtuel (recommandé) :

```bash
python -m venv frozenlake-env
```

3. Activer l’environnement :

* Windows :

```bash
frozenlake-env\Scripts\activate
```

* Linux/Mac :

```bash
source frozenlake-env/bin/activate
```

4. Installer les dépendances :

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Utilisation

1. **Entraîner l’agent :**

```bash
python src/train.py
```

* La Q-table sera sauvegardée dans `data/q_table.npy`.

2. **Vérifier la Q-table :**

```bash
python src/check_qtable.py
```

3. **Afficher la politique optimale :**

```bash
python src/show_policy.py
```

4. **Tester l’agent :**

```bash
python src/test_agent.py
```

---

## Scripts principaux

* `train.py` : Entraîne l’agent avec Q-learning.
* `check_qtable.py` : Affiche la Q-table sauvegardée.
* `show_policy.py` : Affiche la politique optimale par état.
* `test_agent.py` : Teste l’agent sur plusieurs épisodes et affiche les récompenses.
* `render_agent.py` : Visualise l’agent se déplaçant dans la grille (optionnel).

---

## Visualisation

Pour voir l’agent naviguer sur FrozenLake avec rendu graphique :

```bash
python src/render_agent.py
```

> Assurez-vous que `pygame` est installé :

```bash
pip install "gymnasium[toy-text]"
```

---



