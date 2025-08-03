# 🔥 Electric Motor Temperature Prediction (PMSM)

This project predicts the **rotor temperature** of a Permanent Magnet Synchronous Motor (PMSM) using machine learning techniques. It uses various operational parameters (like voltage, current, speed, etc.) as input and outputs the predicted rotor temperature.

---

## 📌 Project Objective

Permanent Magnet Synchronous Machines (PMSMs) are widely used in industrial, automotive, and commercial systems due to their efficiency and reliability. Predicting rotor temperature helps in ensuring motor safety, performance, and extending operational life.

This ML-based Flask app allows users to input real-time motor parameters and get a predicted rotor temperature instantly.

---

## 💡 Key Features

- Predict rotor temperature based on real motor parameters  
- Trained using models like Linear Regression, Decision Tree, Random Forest, SVM  
- Selected best-performing model saved as `best_model.pkl`  
- Integrated with a modern Flask-based frontend UI  
- Input validation and fallback prediction for safety  
- Deployed locally, extendable for edge device integration  

---

## 🛠 Tech Stack & Requirements

- Python 3.10+
- Flask 3.1.1
- Scikit-learn 1.6.1
- Pandas 2.2.2
- NumPy 2.0.2
- Joblib for model serialization
- HTML/CSS for frontend UI

---

## 📦 Installed Packages

| Package         | Version   |
|-----------------|-----------|
| Flask           | 3.1.1     |
| pandas          | 2.2.2     |
| numpy           | 2.0.2     |
| scikit-learn    | 1.6.1     |
| scipy           | 1.16.0    |
| joblib          | 1.5.1     |
| Jinja2          | 3.1.6     |
| Werkzeug        | 3.1.3     |
| blinker         | 1.9.0     |
| python-dateutil | 2.9.0.post0 |
| pytz            | 2025.2    |
| tzdata          | 2025.2    |
| others          | click, colorama, MarkupSafe, etc.

## 🚀 How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/BHARTIYAYASH/electric-motor-temp-vit.git
cd motor-temp-prediction
```

### 2. Create a Virtual Environment and Activate It
```bash
# Create virtual environment
python -m venv env

# Activate on Windows
env\Scripts\activate

# Activate on macOS/Linux
source env/bin/activate
```

### 3. Install All Required Packages
```bash
pip install -r requirements.txt
```

### 4. Ensure the Model File Exists
Make sure the file `best_model.pkl` (your trained ML model) is present in the project root directory.

### 5. Run the Flask App
```bash
python app.py
```

### 6. Access the App in Your Browser
Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🧪 Sample Inputs for Prediction

You can use the following values to test the prediction:

| **Feature**      | **Sample Value** | **Description** |
|------------------|------------------|-----------------|
| `u_q`            | 50.0            | Q-axis voltage (V) |
| `coolant`        | 35.0            | Coolant temperature (°C) |
| `stator_winding` | 60.0            | Stator winding temperature (°C) |
| `u_d`            | 48.0            | D-axis voltage (V) |
| `stator_tooth`   | 55.0            | Stator tooth temperature (°C) |
| `motor_speed`    | 1475.0          | Motor speed (RPM) |
| `i_d`            | 1.2             | D-axis current (A) |
| `i_q`            | 0.8             | Q-axis current (A) |
| `stator_yoke`    | 52.0            | Stator yoke temperature (°C) |
| `torque`         | 42.0            | Motor torque (Nm) |

## ✅ Sample Output
```
Predicted Rotor Temperature: 74.38°C
```


---

