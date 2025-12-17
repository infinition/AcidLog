import time
import json
import random
import os
from datetime import datetime

# --- CONFIGURATION ---
LOG_FILE = "app_logs.log"  # Le fichier à surveiller dans AcidLog
DELAY_RANGE = (0.1, 2.0)    # Délai entre chaque log (en secondes)
BATCH_CHANCE = 0.1          # Chance de générer une rafale d'événements

# Modèles de messages pour les règles de détection d'AcidLog
TEMPLATES = [
    {"level": "info", "msg": "User login success: user_{id}", "weight": 60},
    {"level": "warning", "msg": "Timeout observed on gateway node_{id}", "weight": 20},
    {"level": "high", "msg": "Failed password attempt for root from {ip}", "weight": 15},
    {"level": "critical", "msg": "CRITICAL: SQL Injection attempt detected from {ip}", "weight": 5},
]

IPS = ["192.168.1.45", "10.0.0.12", "45.67.23.12", "185.23.12.90"]

def generate_log():
    # Sélection d'un template basé sur le poids (probabilité)
    template = random.choices(TEMPLATES, weights=[t["weight"] for t in TEMPLATES])[0]
    
    # Remplissage des variables
    log_msg = template["msg"].format(
        id=random.randint(100, 999),
        ip=random.choice(IPS)
    )
    
    # Format compatible AcidLog : [YYYY-MM-DD HH:MM:SS] Message
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {log_msg}\n"
    
    return log_line

def main():
    print(f"🔥 AcidLog Generator démarré...")
    print(f"📁 Écriture dans : {os.path.abspath(LOG_FILE)}")
    print(f"🚀 Appuyez sur Ctrl+C pour arrêter.")

    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, 'w').close()

    try:
        while True:
            # Simulation de pics d'activité
            loops = random.randint(5, 15) if random.random() < BATCH_CHANCE else 1
            
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                for _ in range(loops):
                    line = generate_log()
                    f.write(line)
                    f.flush() # Force l'écriture sur le disque
                    print(f"Log généré : {line.strip()}")
            
            time.sleep(random.uniform(*DELAY_RANGE))
            
    except KeyboardInterrupt:
        print("\n🛑 Générateur arrêté.")

if __name__ == "__main__":
    main()