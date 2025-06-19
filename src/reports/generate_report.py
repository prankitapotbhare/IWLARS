# Report generation logic (placeholder) 

import os
import json
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from reports.charts import (
    pie_chart_status_distribution, bar_chart_volumes, line_chart_balance, scatter_weight_volume, histogram_volumes
)
from reports.qr_code import generate_qr_code

def collect_analytics(processed_dir):
    analytics = []
    for fname in os.listdir(processed_dir):
        if fname.endswith('_analytics.json'):
            with open(os.path.join(processed_dir, fname)) as f:
                data = json.load(f)
                data['wagon_id'] = fname.replace('_analytics.json', '')
                analytics.append(data)
    return analytics

def aggregate_stats(analytics):
    total_wagons = len(analytics)
    total_load = sum(a['metrics']['weight'] for a in analytics)
    total_volume = sum(a['metrics']['volume'] for a in analytics)
    avg_balance = sum(np.linalg.norm(a['metrics']['centroid'][:2]) for a in analytics) / total_wagons if total_wagons else 0
    status_counts = {}
    for a in analytics:
        status = a['status']
        status_counts[status] = status_counts.get(status, 0) + 1
    return {
        'total_wagons': total_wagons,
        'total_load': total_load,
        'total_volume': total_volume,
        'avg_balance': avg_balance,
        'status_counts': status_counts
    }

def generate_charts(analytics, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    statuses = [a['status'] for a in analytics]
    volumes = [a['metrics']['volume'] for a in analytics]
    weights = [a['metrics']['weight'] for a in analytics]
    balance_devs = [np.linalg.norm(a['metrics']['centroid'][:2]) for a in analytics]
    # Pie
    pie_path = os.path.join(out_dir, 'status_pie.png')
    pie_chart_status_distribution(aggregate_stats(analytics)['status_counts'], pie_path)
    # Bar
    bar_path = os.path.join(out_dir, 'volume_bar.png')
    bar_chart_volumes(volumes, statuses, bar_path)
    # Line
    line_path = os.path.join(out_dir, 'balance_line.png')
    line_chart_balance(balance_devs, line_path)
    # Scatter
    scatter_path = os.path.join(out_dir, 'weight_volume_scatter.png')
    scatter_weight_volume(weights, volumes, statuses, scatter_path)
    # Histogram
    hist_path = os.path.join(out_dir, 'volume_hist.png')
    histogram_volumes(volumes, hist_path)
    return {
        'pie': pie_path,
        'bar': bar_path,
        'line': line_path,
        'scatter': scatter_path,
        'hist': hist_path
    }

def generate_pdf_report(processed_dir, template_dir, output_pdf, report_url=None):
    analytics = collect_analytics(processed_dir)
    stats = aggregate_stats(analytics)
    chart_dir = os.path.join(processed_dir, 'charts')
    charts = generate_charts(analytics, chart_dir)
    # QR code
    qr_path = None
    if report_url:
        qr_path = os.path.join(chart_dir, 'report_qr.png')
        generate_qr_code(report_url, qr_path)
    # Prepare data for template
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('report.html')
    html_out = template.render(
        stats=stats,
        analytics=analytics,
        charts=charts,
        qr_code=qr_path
    )
    HTML(string=html_out, base_url=template_dir).write_pdf(output_pdf)
    print(f"PDF report generated at {output_pdf}") 