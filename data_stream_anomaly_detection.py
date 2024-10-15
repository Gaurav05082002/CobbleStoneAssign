import numpy as np
from utils import generate_data_stream, detect_anomaly
from visualization import plot_data_stream

def main():
    # Parameters for the data stream
    stream_length = 1000
    window_size = 50
    threshold = 3  # Z-score threshold for anomaly detection

    # Generate simulated data stream with more complex patterns and concept drift
    data_stream = generate_data_stream(stream_length)

    # Initialize lists for storing data points and anomaly flags
    stream_values = []
    anomaly_flags = []
    rolling_means = []
    rolling_stds = []

    # Stream simulation
    for index, value in enumerate(data_stream):
        stream_values.append(value)
        
        # Detect anomaly using Z-score
        if index >= window_size:
            is_anomaly, mean, std_dev = detect_anomaly(stream_values, window_size, threshold)
            anomaly_flags.append(is_anomaly)
            rolling_means.append(mean)
            rolling_stds.append(std_dev)
        else:
            anomaly_flags.append(False)
            rolling_means.append(np.mean(stream_values))
            rolling_stds.append(np.std(stream_values))

        # Real-time visualization
        plot_data_stream(stream_values, anomaly_flags, rolling_means, rolling_stds)
    
if __name__ == "__main__":
    main()
