import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Set seaborn style for better visuals
sns.set(style="whitegrid")

def plot_data_stream(stream_values, anomaly_flags, rolling_means, rolling_stds):
    """
    Real-time visualization of the data stream and anomaly detection.
    Displays data, anomalies, rolling mean, and rolling standard deviation.
    """
    plt.clf()
    
    # Plot the data stream
    plt.plot(stream_values, label='Data Stream', color='blue', alpha=0.6)
    
    # Highlight anomalies with red markers
    anomalies = [value if flag else None for value, flag in zip(stream_values, anomaly_flags)]
    plt.scatter(range(len(anomalies)), anomalies, color='red', label='Anomalies', s=50)
    
    # Plot rolling mean and rolling standard deviation
    plt.plot(rolling_means, label='Rolling Mean', color='green', linestyle='--')
    plt.fill_between(range(len(stream_values)),
                     np.array(rolling_means) - np.array(rolling_stds),
                     np.array(rolling_means) + np.array(rolling_stds),
                     color='yellow', alpha=0.3, label='±1 Standard Deviation')
    
    plt.legend(loc='upper right')
    plt.title('Real-Time Data Stream with Anomalies')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.pause(0.01)
    plt.draw()

# Initialize the plot
plt.ion()
plt.figure(figsize=(12, 6))
