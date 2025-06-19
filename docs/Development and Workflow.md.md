## 1. Project Development Plan

### 1.1. Overview & Phases

We'll build IWLARS in four major phases, each mapping to a clear deliverable:

1. **Environment & Sensor I/O Module**
2. **Preprocessing & Segmentation Module**
3. **Analytics & Report Generation Module**
4. **Cloud Integration & Optional Dashboard**

### 1.2. Technologies & Tools

| Layer                   | Technology / Library                                |Purpose                                                 |
| ----------------------- | --------------------------------------------------- | ------------------------------------------------------ |
| **Language**            | Python 3.10+                                        | Core logic, rapid development                          |
| **Point Cloud I/O**     | Open3D                                              | Read/write, visualize, filter, segment                 |
| **Numerical Computing** | NumPy, Pandas                                       | Math operations, tabular data                          |
| **PDF Generation**      | WeasyPrint (HTML → PDF), ReportLab                  | Clean, CSS-styled PDF reports                          |
| **Charting**            | Matplotlib                                          | Generate pie/bar/line/scatter/histograms               |
| **API & Cloud Sync**    | FastAPI + Uvicorn, boto3 (AWS S3) or firebase-admin | Expose endpoints, upload/download data                 |
| **Optional Frontend**   | React.js / Next.js + Chart.js/Recharts              | Dashboard for report browsing & analytics              |
| **CI/CD & Deployment**  | GitHub Actions, Docker, AWS EC2 / ECS / Lambda      | Automated tests, containerization, scalable deployment |
| **Version Control**     | Git                                                 | Codebase management, collaboration                     |

### 1.3. System Structure

```
┌────────────────────────────────────────────────────────────┐
│                       iwlars/                              │
│ ┌─────────┐   ┌────────────┐   ┌──────────────┐            │
│ │ sensors/│   │ processing/│   │  analytics/  │            │
│ └─────────┘   └────────────┘   └──────────────┘            │
│     │              │                 │                     │
│     ▼              ▼                 ▼                     │
│  src/main.py ──► filter_ground.py ──► compute_metrics.py   │
│                    segment_wagons.py    classify_status.py │
│                                                            │
│ ┌─────────┐        ┌──────────────┐                        │
│ │ reports/│◄───────┤ charts.py    │                        │
│ └─────────┘        └──────────────┘                        │
│     │ generate_report.py                                   │
│     ▼                                                      │
│  /templates/report.html                                    │
│                                                            │
│ ┌────────────────┐   ┌───────────────────────────────┐     │
│ │ api/           │   │ optional_frontend/            │     │
│ │ └ main_api.py  │   │ └ components/                 │     │
│ └────────────────┘   └───────────────────────────────┘     │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

* **`sensors/`** — interfaces or file-based simulators for LiDAR/IMU
* **`processing/`** — ground removal, noise filtering, wagon segmentation
* **`analytics/`** — volume, weight, balance, status classification
* **`reports/`** — chart generation + PDF assembly using HTML templates
* **`api/`** — FastAPI endpoints to trigger processing or fetch results
* **`optional_frontend/`** — React-based dashboard to list/download reports

---

## 2. Step-by-Step Development Workflow with Timeline (1 Month)

| Week | Focus                            | Deliverables                                                                                                                                                                                                                                                         |
| ---- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1    | **Environment & Sensor I/O**     | • Folder structure, CI/CD pipelines, `requirements.txt`<br>• Basic data loader for LiDAR/IMU (file or socket)<br>• Unit test: load & visualize sample point cloud                                                                                                    |
| 2    | **Preprocessing & Segmentation** | • `filter_ground.py` (RANSAC plane + noise filter)<br>• `segment_wagons.py` (gap detection or clustering)<br>• Tests: verify ground removal & correct wagon splits on sample data                                                                                    |
| 3    | **Analytics & Charting**         | • `compute_metrics.py`: volume (convex hull), weight, balance<br>• `status.py`: rule-based classification<br>• `charts.py`: pie, bar, line, scatter, histogram functions + unit tests                                                                                |
| 4    | **Report, API & Deployment**     | • `generate_report.py`: assemble HTML template → PDF (WeasyPrint), embed charts + QR code<br>• `main_api.py`: FastAPI end-points to start a scan and fetch report URLs<br>• Dockerfile + GitHub Actions for build & deploy<br>• (Optional) React dashboard prototype |

### Week 1: Environment & Sensor I/O

1. **Setup**
   * Initialize Git repo, Dockerfile
   * `requirements.txt`, pre-commit, linting (flake8)

2. **Sensor Simulators**
   * File-based loader for PCD + CSV IMU
   * Basic socket listener stub (UDP/TCP)

3. **Validation**
   * Run `src/main.py` to load & visualize sample data with Open3D

### Week 2: Preprocessing & Segmentation

1. **Ground Filtering**
   * Implement RANSAC plane segmentation in `filter_ground.py`
   * Add radius/voxel noise reduction

2. **Wagon Segmentation**
   * Detect gaps via Euclidean clustering or temporal gaps
   * Assign incremental wagon IDs, store per-wagon PCD files

3. **Tests**
   * Feed known multi-wagon sample → assert correct wagon counts & splits

### Week 3: Analytics & Charting

1. **Metrics Computation**
   * Convex hull volume, centroid → L-R & T-B deviations
   * Weight = volume × density + tilt compensation

2. **Classification Rules**
   * Empty/Normal/Overloaded/Unbalanced in `status.py`
   * Configurable thresholds via `config.yaml`

3. **Chart Generation**
   * Use Matplotlib to generate PNGs for each chart type

4. **Unit Tests**
   * Synthetic point clouds → known volumes/weights/status

### Week 4: Report, API & Deployment

1. **Report Assembly**
   * HTML Jinja template matching sample layout
   * Insert tables, embed chart PNGs, add QR code linking to report URL
   * Render to PDF via WeasyPrint

2. **FastAPI Integration**
   * `POST /scan` → trigger pipeline; returns scan ID
   * `GET /report/{scan_id}` → returns PDF URL

3. **Containerization & CI**
   * Dockerfile: multi-stage build for Python deps + code
   * GitHub Actions: lint, test, build, push image to registry

4. **Deployment**
   * Deploy container to AWS ECS / EC2, configure environment vars for S3 or Firebase
   * (Optional) Deploy React frontend to Netlify or S3+CloudFront

---

## 3. Real-World Workflow and User Experience

### 3.1. Operator Interaction Flow

```text
[Train Approaches] 
       ↓ (Hardware Trigger or Auto-Detect)
[Device Starts Scan → Streams LiDAR+IMU Frames]
       ↓ (Auto)
[Filter → Segment → Analyze → Generate Report]
       ↓ (Auto)
[Upload to Cloud Storage]
       ↓ (Notification / API Response)
[Operator Views / Downloads Report]
```

1. **Auto Trigger**

   * IR beam break or track-mounted motion sensor triggers scan start
   * Alternatively, software monitors LiDAR and auto-starts when "object density" > threshold

2. **Data Capture & Processing**

   * Scanning device (Jetson/RPi/PC) receives raw data → streams into Python pipeline
   * Within seconds, it removes ground, splits wagons, computes metrics

3. **Report Generation & Upload**

   * PDF rendered on-device or in the cloud
   * Uploaded to AWS S3 (public/private bucket) or Firebase Storage
   * System sends an HTTP callback or email to operator with report link

4. **Dashboard Access (Optional)**

   * Operator logs into a web UI (React) at `https://iwlars.example.com`
   * Sees list of recent scans, their status, and "Download PDF" buttons
   * Can filter by date, train ID, or anomaly type

### 3.2. Deployment in the Field

* **Hardware**:

  * LiDAR + IMU wired to an edge device (Jetson Xavier NX recommended)
  * UPS backup for power stability
* **Network**:

  * 4G/5G or Ethernet link to cloud
  * VPN for secure API access
* **Maintenance**:

  * Auto-updates via Docker image pull
  * Health-check endpoint (`/health`) monitored by Prometheus or AWS CloudWatch
  * Detailed logs shipped to ELK stack for on-site troubleshooting

---

### ASCII Workflow Diagram

```
   ┌──────────────┐      ┌────────────┐      ┌───────────────┐
   │ LiDAR + IMU  │─────▶│ Edge Device│─────▶│ Cloud Storage │
   │  Sensors     │      │  (Python)  │      │ (S3 / Firebase)│
   └──────────────┘      └────────────┘      └───────────────┘
         │                     │                    │
         │                     │                    │
         ▼                     ▼                    ▼
  [Point Stream]       [Process & Analyze]    [PDF + JSON]
                             │
                             ▼
                     [FastAPI Notification]
                             │
                             ▼
                     [Operator Dashboard]
```

---

**This plan** ensures you have:

* A **clear month-long roadmap** with week-by-week goals
* An **actionable tech stack** and project structure
* A **seamless user experience**, from train pass to report download
* **Deployment guidance** for real-world edge/cloud environments

## Simulating Real-Time Wagon Data and Processing

To test the IWLARS pipeline as if data is arriving from a moving train in real time, follow this simulation approach:

1. **Prepare Sample Data:**
   - Place sequential LiDAR (.pcd) and IMU (.csv) files in `data/raw/frames/`. Each file represents a new sensor frame.

2. **Timed Data Loader:**
   - Implement a loader in `src/sensors/data_loader.py` that watches the directory and, at fixed intervals (e.g., every 1 second), loads the next file and passes it to the processing pipeline.

3. **Pipeline Trigger:**
   - The loader calls the processing functions (ground filtering, segmentation, analytics, etc.) for each frame, simulating real-time data flow.

4. **Automated Reporting:**
   - After all frames are processed, the pipeline can generate reports as in production.

5. **Optional API Trigger:**
   - You can expose a FastAPI endpoint to start the simulation from a dashboard or script.

**Summary Diagram:**

```mermaid
flowchart LR
    A[Sample LiDAR/IMU Files] -->|Timer/Watcher| B[Data Loader]
    B --> C[Processing Pipeline]
    C --> D[Analytics]
    D --> E[Report Generation]
    E --> F[PDF/Charts Output]
```

This approach allows for realistic, repeatable, and modular testing of the full IWLARS workflow.