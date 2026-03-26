from monitor_metrics import check_resources
from scaler import launch_instance
import time
import yaml

with open("config/config.yaml") as f:
	config = yaml.safe_load(f)

last_scaled = 0
instance_created = False

while True:
	if check_resources(config["threshold"]):
		now = time.time()
		if now - last_scaled > config["cooldown"]:
			print("[ALERT] Scaling triggered")
			launch_instance(config)
			last_scaled = now
			instance_created = True
	time.sleep(5)
