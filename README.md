# Raspberry Pi Dashcam

Ce projet permet de transformer un Raspberry Pi en une dashcam simple et efficace. Il enregistre en continu des vidéos en boucle et supprime les plus anciennes pour gérer l'espace de stockage.

## 🚀 Fonctionnalités
- 📹 Enregistrement en continu avec des vidéos de 5 minutes
- 🗑️ Suppression automatique des vidéos les plus anciennes
- 🕒 Ajout d'un horodatage aux fichiers vidéo
- 🛠️ Facile à modifier et à améliorer (ajout de GPS, détection de choc, accès WiFi...)

## 📦 Matériel requis
- Raspberry Pi Zero W (ou autre modèle compatible)
- Module caméra CSI pour Raspberry Pi
- Carte microSD (32 Go minimum recommandé)
- Alimentation 5V (via allume-cigare de voiture ou autre source fiable)
- (Optionnel) Module GPS USB pour ajouter la localisation aux vidéos

## 🛠️ Installation
1. **Cloner ce dépôt sur votre Raspberry Pi** :
   ```bash
   git clone https://github.com/votre-utilisateur/raspberry-pi-dashcam.git
   cd raspberry-pi-dashcam
   ```
2. **Installer les dépendances Python** :
   ```bash
   pip install picamera2
   ```
3. **Créer le dossier de stockage des vidéos** :
   ```bash
   mkdir -p /home/pi/dashcam_videos
   ```
4. **Exécuter le script** :
   ```bash
   python3 dashcam.py
   ```

## 🔧 Configuration
- Modifier `MAX_VIDEOS` dans `dashcam.py` pour ajuster le nombre maximal de vidéos stockées.
- Modifier `VIDEO_DURATION` pour ajuster la durée des vidéos enregistrées.

## 🛠️ Améliorations possibles
- 📡 Ajouter un accès WiFi pour récupérer les vidéos à distance
- 📍 Ajouter un module GPS pour incruster la position et la vitesse sur la vidéo
- 🚦 Ajouter une détection de mouvement ou de choc pour enregistrer seulement en cas d'incident

## 📜 Licence
Ce projet est sous licence MIT. Vous êtes libre de l'utiliser et de le modifier à votre convenance !

---

🔥 **Un projet fait avec passion pour allier Raspberry Pi et voiture !** 🚗💨

