# preprocess.py - Data preprocessing utilities

import pandas as pd
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

def preprocess_data(df):
    # Drop label if it exists
    features = df.drop(['Class'], axis=1, errors='ignore')

    # Normalize Amount and Time if present
    if 'Amount' in features.columns:
        features['Amount'] = scaler.fit_transform(features[['Amount']])
    if 'Time' in features.columns:
        features['Time'] = scaler.fit_transform(features[['Time']])

    # Return only known model features
    return features
