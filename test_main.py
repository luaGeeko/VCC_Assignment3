from test_monitoring import check_resources, should_scale
from test_scaler import launch_instance
import time

while True:
    if check_resources() and should_scale():
        print("[ALERT] Threshold exceeded → Scaling...")
        launch_instance()

    time.sleep(5)
