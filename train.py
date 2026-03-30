import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

# Load data
df = pd.read_csv("yarn_failure_logs.csv")

# Preprocess
df = df.drop(columns=["timestamp"])
df["node_health"] = df["node_health"].astype(int)

X = df.drop("label", axis=1)
y = df["label"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train
model = XGBClassifier(max_depth=5)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))