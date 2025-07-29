import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle
import random

MODEL_PATH = "modelo.pkl"
model = None

def generate_data():
    # simulacao de dados
    data = []
    for _ in range(1000):
        data.append([random.randint(1, 10)])  # normal
    for _ in range(50):
        data.append([random.randint(100, 200)])  # anormal
    return pd.DataFrame(data, columns=["requests"])

def train_model():
    global model
    df = generate_data()
    model = IsolationForest(contamination=0.05)
    model.fit(df)
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

def predict_anomaly(request_count):
    global model
    if not model:
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
    df = pd.DataFrame([[request_count]], columns=["requests"])
    return model.predict(df)[0] == -1
