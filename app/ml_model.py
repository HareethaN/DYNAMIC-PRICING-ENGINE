import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(_file_), "../models/conversion_model.joblib")

def train_model():
    df = pd.read_csv(os.path.join(os.path.dirname(_file_), "../data/sample_events.csv"))
    X = df.drop(columns=["purchased"])
    y = df["purchased"]

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.05, max_depth=5)
    clf.fit(X_train, y_train)
    preds = clf.predict_proba(X_val)[:, 1]
    print("Validation AUC:", roc_auc_score(y_val, preds))
    joblib.dump(clf, MODEL_PATH)
    return clf

def load_model():
    if not os.path.exists(MODEL_PATH):
        return train_model()
    return joblib.load(MODEL_PATH)
