import time
import pandas as pd
from utils.preprocess import preprocess_data
from utils.alert import send_alert

def simulate_transactions(model, interval=3):
    flagged = []
    df = pd.read_csv('data/real_time_feed.csv')  # You can change this path
    for index, row in df.iterrows():
        sample = pd.DataFrame([row])
        processed = preprocess_data(sample)
        prediction = model.predict(processed)[0]
        if prediction == 1:
            flagged_msg = f"Transaction ID {index} flagged as fraud"
            flagged.append(flagged_msg)
            send_alert(row)
        time.sleep(interval)
        if len(flagged) >= 5:
            break
    return flagged
