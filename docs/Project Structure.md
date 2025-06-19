iwlars/
│
├── src/
│   ├── sensors/
│   │   ├── __init__.py
│   │   ├── lidar_interface.py
│   │   ├── imu_interface.py
│   │   ├── data_loader.py         # For file-based simulation
│   │   └── buffer.py              # Local buffering logic
│   │
│   ├── processing/
│   │   ├── __init__.py
│   │   ├── filter_ground.py
│   │   ├── noise_filter.py
│   │   └── segment_wagons.py
│   │
│   ├── analytics/
│   │   ├── __init__.py
│   │   ├── compute_metrics.py
│   │   ├── classify_status.py
│   │   └── config.yaml            # Thresholds, densities, etc.
│   │
│   ├── reports/
│   │   ├── __init__.py
│   │   ├── generate_report.py
│   │   ├── charts.py
│   │   ├── qr_code.py
│   │   └── templates/
│   │       └── report.html        # Jinja2/HTML template for PDF
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── main_api.py            # FastAPI endpoints
│   │
│   ├── main.py                    # Pipeline entry point
│   └── utils.py                   # Shared utilities
│
├── data/
│   ├── raw/                       # Raw LiDAR/IMU data
│   ├── processed/                 # Cleaned/segmented data
│   └── reports/                   # Generated PDFs, charts
│
├── tests/
│   ├── sensors/
│   ├── processing/
│   ├── analytics/
│   ├── reports/
│   └── api/
│
├── optional_frontend/
│   ├── components/
│   ├── pages/
│   └── package.json
│
├── .github/
│   └── workflows/
│       └── ci.yml                 # GitHub Actions for CI/CD
│
├── requirements.txt
├── Dockerfile
├── README.md
├── .gitignore
└── .env.example                   # Example environment variables