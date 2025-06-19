# Chart generation logic (placeholder) 

import matplotlib.pyplot as plt
import numpy as np

def pie_chart_status_distribution(status_counts, out_path):
    labels = list(status_counts.keys())
    sizes = list(status_counts.values())
    colors = ['#36a2eb', '#ffcd56', '#ff6384', '#cc65fe']
    plt.figure(figsize=(4,4))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
    plt.title('Wagon Status Distribution')
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

def bar_chart_volumes(volumes, statuses, out_path):
    color_map = {'Normal':'#36a2eb', 'Empty':'#ffcd56', 'Overloaded':'#ff6384', 'Unbalanced':'#cc65fe'}
    colors = [color_map.get(s, '#888888') for s in statuses]
    plt.figure(figsize=(8,4))
    plt.bar(range(len(volumes)), volumes, color=colors)
    plt.xlabel('Wagon Index')
    plt.ylabel('Volume (m³)')
    plt.title('Volume Distribution by Wagon')
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

def line_chart_balance(balance_devs, out_path):
    plt.figure(figsize=(8,4))
    plt.plot(balance_devs, marker='o')
    plt.xlabel('Wagon Index')
    plt.ylabel('Balance Deviation (%)')
    plt.title('Balance Deviation Trend')
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

def scatter_weight_volume(weights, volumes, statuses, out_path):
    color_map = {'Normal':'#36a2eb', 'Empty':'#ffcd56', 'Overloaded':'#ff6384', 'Unbalanced':'#cc65fe'}
    colors = [color_map.get(s, '#888888') for s in statuses]
    plt.figure(figsize=(6,6))
    plt.scatter(volumes, weights, c=colors)
    plt.xlabel('Volume (m³)')
    plt.ylabel('Weight (tons)')
    plt.title('Weight vs Volume')
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

def histogram_volumes(volumes, out_path):
    plt.figure(figsize=(6,4))
    plt.hist(volumes, bins=10, color='#36a2eb', edgecolor='black')
    plt.xlabel('Volume (m³)')
    plt.ylabel('Count')
    plt.title('Histogram of Wagon Volumes')
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close() 