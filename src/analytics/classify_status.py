# Status classification logic (placeholder) 

import numpy as np
import yaml
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

CONFIG = load_config()

def classify_status(metrics):
    volume = metrics['volume']
    weight = metrics['weight']
    centroid = np.array(metrics['centroid'])
    empty_th = CONFIG.get('empty_threshold', 0.1)
    overload_th = CONFIG.get('overload_threshold', 1.2)
    unbalanced_th = CONFIG.get('unbalanced_threshold', 0.15)
    # Simple unbalance: deviation from center in X or Y
    deviation = np.linalg.norm(centroid[:2])
    if volume < empty_th:
        return 'Empty'
    elif deviation > unbalanced_th:
        return 'Unbalanced'
    elif weight > overload_th:
        return 'Overloaded'
    else:
        return 'Normal' 