import psutil
import time

THRESHOLD = 75
COOLDOWN = 60  # seconds

last_scaled_time = 0

def check_resources():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    
    print(f"[INFO] CPU: {cpu}% | MEM: {memory}%")
    
    return cpu > THRESHOLD or memory > THRESHOLD


def should_scale():
    global last_scaled_time
    now = time.time()
    
    if now - last_scaled_time > COOLDOWN:
        last_scaled_time = now
        return True
    return False
