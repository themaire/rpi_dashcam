import os
import time
import picamera2
from datetime import datetime

# Dossier de stockage des vidéos
VIDEO_FOLDER = "/home/pi/dashcam_videos"
MAX_VIDEOS = 10  # Nombre maximum de vidéos à stocker
VIDEO_DURATION = 300  # Durée de chaque vidéo en secondes (5 min)

# Création du dossier si inexistant
os.makedirs(VIDEO_FOLDER, exist_ok=True)

# Initialisation de la caméra
camera = picamera2.Picamera2()
camera_config = camera.create_video_configuration()
camera.configure(camera_config)

# Fonction pour supprimer les vidéos les plus anciennes
def clean_old_videos():
    videos = sorted(os.listdir(VIDEO_FOLDER))
    while len(videos) > MAX_VIDEOS:
        os.remove(os.path.join(VIDEO_FOLDER, videos[0]))
        videos.pop(0)

# Boucle d'enregistrement en continu
try:
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        video_path = os.path.join(VIDEO_FOLDER, f"video_{timestamp}.h264")
        
        print(f"Enregistrement en cours : {video_path}")
        camera.start_recording(video_path)
        time.sleep(VIDEO_DURATION)
        camera.stop_recording()
        
        clean_old_videos()
except KeyboardInterrupt:
    print("Arrêt de la dashcam")
    camera.close()
