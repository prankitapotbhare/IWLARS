
# Intelligent Wagon Load Analysis & Reporting System (IWLARS)

## Overview
IWLARS is an end-to-end, automated platform for analyzing the load status of moving train wagons using LiDAR and IMU sensors. It delivers real-time, actionable insights for logistics, safety, and operational efficiency in the railway sector. The system covers the entire pipeline: from sensor data acquisition, through advanced analytics, to PDF report generation and cloud distribution, with optional dashboard and API integration.

## Key Features
- **Automated Data Capture:** Real-time acquisition of point cloud and motion data as trains pass a checkpoint.
- **Advanced Processing:** Ground/noise filtering, wagon segmentation, and metric computation (volume, weight, balance).
- **Analytics & Visualization:** Rule-based status classification (Normal, Empty, Overloaded, Unbalanced) and rich chart generation.
- **Automated Reporting:** Generates comprehensive, styled PDF reports with summary statistics, per-wagon details, and visualizations.
- **Cloud Integration:** Uploads reports to AWS S3 or Firebase, with API notifications and secure access.
- **Optional Dashboard:** React-based frontend for browsing, filtering, and tracking historical reports and trends.
- **Modular & Scalable:** Designed for reliability, scalability, and minimal operator intervention.

## Project Structure
```
iwlars/
│
├── src/
│   ├── sensors/            # LiDAR/IMU interfaces, simulators, data loader
│   ├── processing/         # Ground removal, noise filtering, wagon segmentation
│   ├── analytics/          # Metrics calculation, status classification
│   ├── reports/            # Chart generation, PDF assembly, templates
│   ├── api/                # FastAPI endpoints
│   ├── main.py             # Pipeline entry point
│   └── utils.py            # Shared utilities
│
├── data/
│   ├── raw/                # Raw sensor data (PCD, LAS, CSV)
│   ├── processed/          # Segmented wagon data
│   └── reports/            # Generated PDF reports
│
├── tests/                  # Unit/integration tests for all modules
├── optional_frontend/      # React dashboard prototype
├── Dockerfile              # Containerization
├── requirements.txt        # Python dependencies
└── docs/                   # Documentation, sample reports, workflow diagrams
```

## Main Modules
- **sensors/**: Sensor I/O, simulation, and data loading
- **processing/**: Point cloud cleaning, ground/noise filtering, wagon segmentation
- **analytics/**: Metric computation (volume, weight, balance), status classification
- **reports/**: Chart generation, PDF assembly, HTML templates
- **api/**: FastAPI endpoints for scan triggering, report retrieval, and health checks
- **optional_frontend/**: (Optional) React dashboard for report browsing and analytics

## System Workflow
1. **Data Acquisition:** LiDAR and IMU sensors capture data as a train passes; data is streamed to an edge device.
2. **Preprocessing:** Ground and noise are filtered; point cloud is segmented into individual wagons.
3. **Analytics:** For each wagon, compute volume, estimate weight, assess load balance, and classify status.
4. **Reporting:** Compile results into an HTML report, render as PDF, and generate charts.
5. **Cloud Distribution:** Upload PDF to cloud storage and notify operator via API/email/dashboard.
6. **User Interaction:** Operator receives notification, reviews report, and can access historical data via dashboard.

## Technologies & Tools
| Layer                   | Technology / Library                                | Purpose                                                 |
| ----------------------- | --------------------------------------------------- | ------------------------------------------------------- |
| **Language**            | Python 3.10+                                        | Core logic, rapid development                           |
| **Point Cloud I/O**     | Open3D                                              | Read/write, visualize, filter, segment                  |
| **Numerical Computing** | NumPy, Pandas                                       | Math operations, tabular data                           |
| **PDF Generation**      | WeasyPrint (HTML → PDF), ReportLab                  | Clean, CSS-styled PDF reports                           |
| **Charting**            | Matplotlib                                          | Generate pie/bar/line/scatter/histograms                |
| **API & Cloud Sync**    | FastAPI + Uvicorn, boto3 (AWS S3) or firebase-admin | Expose endpoints, upload/download data                  |
| **Optional Frontend**   | React.js / Next.js + Chart.js/Recharts              | Dashboard for report browsing & analytics               |
| **CI/CD & Deployment**  | GitHub Actions, Docker, AWS EC2 / ECS / Lambda      | Automated tests, containerization, scalable deployment  |
| **Version Control**     | Git                                                 | Codebase management, collaboration                      |

## Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-org/iwlars.git
cd iwlars
```
### 2. Set Up Virtual Environment (Optional but Recommended)
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
- Copy `.env.example` to `.env` and update values as needed for your environment (e.g., cloud credentials, API keys).

### 4. Prepare Data (Optional for Simulation)
- Place sample LiDAR (`.pcd`, `.las`) and IMU (`.csv`) files in `data/raw/frames/` to simulate real-time data input.

### 5. Run the Main Pipeline
```bash
python src/main.py
```

### 6. Access Reports
- Generated PDF reports will be available in `data/reports/` and/or uploaded to your configured cloud storage.
- If the dashboard is enabled, access it via the provided URL.

## Additional Resources
- See `docs/` for detailed workflow, architecture, and sample reports.
- For development phases, system diagrams, and advanced configuration, refer to:
  - `docs/Intelligent Wagon Load Analysis & Reporting System (IWLARS).md`
  - `docs/Development Plan.md`
  - `docs/System Workflow.md`
  - `docs/Project Structure.md`