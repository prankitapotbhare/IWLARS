from sensors.data_loader import simulate_data_stream
import os
import open3d as o3d
import numpy as np
import json
from processing.filter_ground import remove_ground_plane
from processing.noise_filter import remove_noise
from processing.segment_wagons import segment_wagons
from analytics.compute_metrics import compute_metrics
from analytics.classify_status import classify_status
from reports.generate_report import generate_pdf_report
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

# Add laspy for .las support
try:
    import laspy
except ImportError:
    laspy = None
    print("[WARNING] laspy not installed. .las files will not be supported.")

def load_point_cloud(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pcd' or ext == '.ply':
        return o3d.io.read_point_cloud(file_path)
    elif ext == '.las':
        if laspy is None:
            raise ImportError("laspy is required for .las file support.")
        las = laspy.read(file_path)
        points = np.vstack((las.x, las.y, las.z)).transpose()
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(points)
        return pcd
    else:
        raise ValueError(f"Unsupported file format: {ext}")

def process_frame(file_path):
    print(f"[SIMULATION] Processing frame: {os.path.basename(file_path)}")
    ext = os.path.splitext(file_path)[1].lower()
    if ext in ['.pcd', '.ply', '.las']:
        try:
            # 1. Load point cloud
            pcd = load_point_cloud(file_path)
            # 2. Remove noise
            pcd = remove_noise(pcd)
            # 3. Remove ground
            pcd, _ = remove_ground_plane(pcd)
            # 4. Segment wagons
            wagons = segment_wagons(pcd)
            # 5. Save each wagon and compute analytics
            processed_dir = os.path.join("data", "processed")
            os.makedirs(processed_dir, exist_ok=True)
            for idx, wagon in enumerate(wagons):
                base_name = f"{os.path.splitext(os.path.basename(file_path))[0]}_wagon{idx+1}"
                out_path = os.path.join(processed_dir, f"{base_name}.pcd")
                o3d.io.write_point_cloud(out_path, wagon)
                # Analytics
                metrics = compute_metrics(wagon)
                status = classify_status(metrics)
                analytics = {"metrics": metrics, "status": status}
                analytics_path = os.path.join(processed_dir, f"{base_name}_analytics.json")
                with open(analytics_path, 'w') as f:
                    json.dump(analytics, f, indent=2)
                print(f"  Saved wagon {idx+1} to {out_path} and analytics to {analytics_path}")
        except Exception as e:
            print(f"[ERROR] Failed to process {file_path}: {e}")
    else:
        print("[SKIP] Only .pcd, .ply, and .las files are processed in this step.")

class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            ext = os.path.splitext(event.src_path)[1].lower()
            if ext in ['.pcd', '.ply', '.las']:
                print(f"[WATCHDOG] New file detected: {event.src_path}")
                process_frame(event.src_path)
                # After processing, generate report
                processed_dir = os.path.join("data", "processed")
                template_dir = os.path.join("src", "reports", "templates")
                output_pdf = os.path.join(processed_dir, "iwlars_report.pdf")
                # You can set a real cloud URL here if available
                report_url = None
                generate_pdf_report(processed_dir, template_dir, output_pdf, report_url=report_url)


def main():
    print("IWLARS pipeline starting and monitoring for new files...")
    data_dir = os.path.join("data", "raw", "frames")
    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, data_dir, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main() 