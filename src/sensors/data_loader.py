# File-based loader for LiDAR/IMU data (placeholder) 
import time
import os

def simulate_data_stream(data_dir, process_func, interval=1.0):
    files = sorted(os.listdir(data_dir))
    for fname in files:
        if fname.endswith('.pcd') or fname.endswith('.csv'):
            print(f"Processing {fname}")
            process_func(os.path.join(data_dir, fname))
            time.sleep(interval) 