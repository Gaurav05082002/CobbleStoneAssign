import numpy as np
from scipy import stats
import pandas as pd
import numpy as np
from scipy import stats
import pandas as pd


def generate_data_stream(length):
    """
    Generates a simulated data stream with random noise, seasonal patterns,
    occasional spikes (anomalies), and concept drift.
    """
    np.random.seed(42)
    time = np.arange(0, length)

    # Seasonal pattern with concept drift over time
    seasonal_pattern = 10 * np.sin(0.1 * time) + (time / 100)  # Concept drift
    noise = np.random.normal(0, 1, length)  # Random noise

    # Simulating anomalies by adding spikes at random points
    anomalies = np.random.choice([0, 1], size=length, p=[0.98, 0.02]) * np.random.uniform(20, 40, size=length)

    # Combining all components
    data_stream = seasonal_pattern + noise + anomalies
    return data_stream

def detect_anomaly(data, window_size, threshold):
    """
    Detects anomalies based on the Z-score of the rolling window.
    """
    recent_data = np.array(data[-window_size:])
    mean = np.mean(recent_data)
    std_dev = np.std(recent_data)

    if std_dev == 0:
        return False, mean, std_dev  # Avoid division by zero

    z_score = (data[-1] - mean) / std_dev
    is_anomaly = abs(z_score) > threshold
    return is_anomaly, mean, std_dev
