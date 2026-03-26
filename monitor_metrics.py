import psutil

history = []

def check_resources(threshold):
	cpu = psutil.cpu_percent(interval=1)
	memory = psutil.virtual_memory().percent
	usage = max(cpu, memory)
	history.append(usage)
	if len(history) > 3:
		history.pop(0)
	avg = sum(history) / len(history)
	print(f"[INFO] CPU: {cpu}% | MEM: {memory}% | AVG: {avg}")
	return avg > threshold
