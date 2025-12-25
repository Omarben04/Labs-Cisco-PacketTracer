from netmiko import ConnectHandler
from datetime import datetime

# --- CONFIGURATION ---
# Ici, on simule un routeur. Pour GitHub, ce code suffit à montrer que tu sais faire.
# Si tu avais un vrai lab GNS3 allumé, tu mettrais sa vraie IP ici.
routeur_cisco = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.50',   # IP fictive pour l'exemple
    'username': 'admin',
    'password': 'cisco_password',
    'secret': 'enable_password',
}

print(f"Connexion au routeur {routeur_cisco['host']} en cours...")

try:
    # 1. Connexion SSH
    connexion = ConnectHandler(**routeur_cisco)
    connexion.enable() # Passage en mode privilégié (#)
    
    # 2. Récupération de la configuration
    print("Récupération de la configuration (show run)...")
    config = connexion.send_command("show running-config")
    
    # 3. Création du nom de fichier avec la date
    nom_fichier = f"backup_router_{datetime.now().strftime('%Y-%m-%d')}.txt"
    
    # 4. Sauvegarde dans un fichier texte
    with open(nom_fichier, 'w') as f:
        f.write(config)
    
    print(f"✅ Sauvegarde réussie dans : {nom_fichier}")
    connexion.disconnect()

except Exception as erreur:
    # Si le routeur n'existe pas (ce qui est normal sans GNS3 allumé), on affiche ceci :
    print(f"❌ Erreur de connexion (Normal si GNS3 est éteint) : {erreur}")