# Script d'Automatisation de Sauvegarde Cisco

## 📋 Description
Ce script Python permet de se connecter automatiquement à un routeur Cisco via SSH pour sauvegarder sa configuration courante (`show running-config`).

## 🛠 Fonctionnalités
* Utilisation de la librairie **Netmiko** pour la connexion SSH sécurisée.
* Gestion automatique du mode "Enable".
* Sauvegarde de la configuration dans un fichier texte horodaté (avec la date du jour).
* Gestion des erreurs en cas de perte de connectivité.

## 💻 Comment l'utiliser
1. Installer les dépendances : `pip install netmiko`
2. Modifier l'adresse IP dans le script `backup_config.py`.
3. Lancer le script : `python backup_config.py`