# Efficient Data Stream Anomaly Detection

This project demonstrates real-time anomaly detection in a continuous data stream. The data stream simulates real-world sequences of floating-point numbers with seasonal variations and random noise. Anomalies are flagged based on deviations from expected patterns.

## Instructions

1. Ensure you have Python 3.x installed.
2. Install required dependencies using `pip install -r requirements.txt`.
3. Run the program: `python data_stream_anomaly_detection.py`.
4. For stopping simulation: `ctrl+C`.

## Files

- `data_stream_anomaly_detection.py`: Main script for data stream simulation and anomaly detection.
- `utils.py`: Contains helper functions for data generation and anomaly detection algorithms.
- `visualization.py`: Real-time visualization of the data stream and detected anomalies.

## Algorithm

The selected algorithm is based on **Z-score normalization**, which is effective for detecting outliers by comparing incoming data points to the historical mean and standard deviation. It also adapts to concept drift and seasonal variations using a rolling window.

## External Libraries

- `matplotlib` for real-time plotting.
- `numpy` for efficient numerical computations.
- `scipy` for statistical anomaly detection (Z-score).

## Improvements
### since the assignment says, dont use advance libs so, I have tried to keep it fundamental
The algorithm can be optimized further by incorporating more advanced techniques such as autoencoders, isolation forests, or recurrent neural networks.
