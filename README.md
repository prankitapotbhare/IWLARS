# Intelligent Wagon Load Analysis & Reporting System (IWLARS)

## Overview
IWLARS is an end-to-end system for capturing, processing, analyzing, and reporting train wagon load data using LiDAR and IMU sensors. The system is modular, cloud-integrated, and supports automated PDF report generation.

## Main Modules
- **sensors/**: Sensor I/O and simulation
- **processing/**: Point cloud cleaning, segmentation
- **analytics/**: Metric computation, status classification
- **reports/**: Chart generation, PDF assembly
- **api/**: FastAPI endpoints
- **optional_frontend/**: (Optional) React dashboard

## Setup
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Configure environment variables (see `.env.example`)
4. Run the main pipeline: `python src/main.py`

See docs/ for detailed workflow and architecture. 