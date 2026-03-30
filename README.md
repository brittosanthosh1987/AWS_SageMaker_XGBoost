# AWS_SageMaker_XGBoost
Prediction to find failure jobHow to Run This Project


---

### 🔹 1. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
```

Activate environment:

* Windows:

```bash
venv\Scripts\activate
```

* Mac/Linux:

```bash
source venv/bin/activate
```

---

## ☁️ Run on AWS SageMaker (Optional)

Follow these steps to run this project in AWS SageMaker Studio.

---

### 🔹 1. Open SageMaker AI

* Go to AWS Console
* Search for **SageMaker AI**
* Click **Create Domain**

👉 Use default settings (quick setup)

---

### 🔹 2. Launch Studio

* After domain creation, click **Open Studio**
* Create a new Notebook

---

### 🔹 3. Create Notebook

* Click **Notebook → Create Notebook**
* Choose:

  * Kernel: Python 3 (Data Science)
  * Instance: Default (no need to change)

---

### 🔹 4. Upload Project Files

Upload:

* `train.py`
* `predict.py`
* `requirements.txt`
* `yarn_failure_logs.csv`  

👉 You can drag & drop into the file browser

---

### 🔹 5. Install Dependencies

Open terminal or notebook cell:

```
pip install -r requirements.txt
```

---

### 🔹 6. Run Training Script

```
python train.py
```

👉 Output:

```
Model Accuracy: ~0.91
```

---

### 🔹 7. Run Prediction (Optional)

```
python predict.py
```

---

### 🔹 8. Stop Resources (IMPORTANT)

To avoid charges:

* Stop notebook
* Delete SageMaker Domain after use

---

## 💡 Notes

* No GPU required
* Uses CPU instance
* Low-cost testing


### 🔹 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 3. Run Training Script

```bash
python train.py
```

👉 This will:

* Load dataset
* Train XGBoost model
* Print accuracy

---

### 🔹 5. (Optional) Run Prediction Script

```bash
python predict.py
```

👉 This will:

* Take sample input
* Predict SUCCESS / FAILURE

---

## 📊 Expected Output

```text
Model Accuracy: ~0.91
```

---

## 📂 Project Structure

```

you can change the depth to test it , but real time logs would be easy to get more accuracy . 

yarn-failure-prediction/
│
├── data/
│   └── yarn_failure_logs.csv
├── train.py
├── predict.py
├── requirements.txt
├── README.md
```
s
