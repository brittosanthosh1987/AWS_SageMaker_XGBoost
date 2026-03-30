import pandas as pd
import numpy as np
from xgboost import XGBClassifier

# 1. Load dataset
df = pd.read_csv("yarn_failure_logs.csv")

# 2. Preprocessing (same as train.py)
df = df.drop(columns=["timestamp"])
df["node_health"] = df["node_health"].astype(int)

X = df.drop("label", axis=1)
y = df["label"]

# 3. Train model (quick training for demo)
model = XGBClassifier(max_depth=5)
model.fit(X, y)

# 4. Sample input (manual test case)
# Format: [cpu, memory, retry, failed_tasks, duration, node_health]
sample = np.array([[80, 90, 2, 5, 200, 1]])

# 5. Predict
prediction = model.predict(sample)[0]
probability = model.predict_proba(sample)[0][1]

# 6. Output result
if prediction == 1:
    print("Prediction: FAILURE ❌")
else:
    print("Prediction: SUCCESS ✅")

print("Failure Probability:", round(probability, 2))