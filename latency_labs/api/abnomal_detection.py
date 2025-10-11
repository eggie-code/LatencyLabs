import numpy as np
from sklearn.ensemble import IsolationForest

# anomaly detection function


def detect_anomalies(metrics):
    # Use Isolation Forest to detect anomalies
    isolation_forest = IsolationForest(contamination=0.1)
    anomalies = isolation_forest.fit_predict(metrics)
    return anomalies
