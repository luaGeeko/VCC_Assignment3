import subprocess
import time

def launch_instance(config):
	name = f"auto-vm-{int(time.time())}"
	cmd = [
			"gcloud", "compute", "instances", "create", name, 
			"--zone", config["zone"], 
			"--machine-type", config["machine_type"],
			"--project", config["project"]]
	try:
		subprocess.run(cmd, check=True)
		print(f"[SCALING] Launched VM: {name}")
	except Exception as e:
		print(f"[ERROR] {e}")
