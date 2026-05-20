✍️  README.md

# 🩺 Project Title - Diabetes Glucose Analysis Using CGM and Wearable Sensor Data and Diabetes Glucose Prediction Analysis

## 📌 Project Overview

This project analyzes Continuous Glucose Monitoring (CGM) data along with insulin administration, carbohydrate intake, and wearable sensor data such as heart rate, steps, and calories burned. The dataset is collected from individuals with Type 1 Diabetes and aims to understand how daily lifestyle and physiological factors influence blood glucose levels.

---

## 🎯 Problem Statement

Managing Type 1 Diabetes requires maintaining stable blood glucose levels. However, glucose fluctuations are influenced by multiple factors such as insulin dosage, carbohydrate intake, physical activity, and physiological signals. Understanding these relationships is essential for improving diabetes management and reducing risks of hypoglycemia and hyperglycemia.

---

## 🧠 Business / Research Goal

To analyze how insulin dosage, carbohydrate intake, physical activity, and physiological signals influence blood glucose levels in Type 1 Diabetes patients using CGM and wearable sensor data.
To explore diabetes-related time-series data and build a machine learning model that predicts glucose values using patient, activity, insulin, nutrition, and engineered time-series features.

---

## 📊 Dataset Information

This project uses the **HUPA-UCM Diabetes Dataset**, which contains Continuous Glucose Monitoring (CGM) data and wearable sensor data collected from 25 individuals with Type 1 Diabetes Mellitus (T1DM).

The dataset includes:
- Blood glucose measurements
- Insulin administration records
- Carbohydrate intake
- Physical activity data
- Heart rate measurements
- Calories burned

Data was collected over approximately 14 days using:
- FreeStyle Libre 2 CGMs
- Fitbit Ionic smartwatches

The dataset supports research on glucose prediction, diabetes management, and relationships between physiological and lifestyle factors.

### Key Features:
- `time` → Timestamp of observation
- `glucose` → Continuous glucose monitoring readings
- `calories` → Calories burned
- `heart_rate` → Heart rate measurements
- `steps` → Physical activity (step count)
- `basal_rate` → Basal insulin delivery rate
- `bolus_volume_delivered` → Insulin bolus doses
- `carb_input` → Carbohydrate intake (grams)
- `patient_id` → Unique identifier for each patient

---

## 🛠️ Tools & Technologies Used

- Python 🐍
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Git & GitHub

---

## 📁 Project Structure
diabetes-glucose-analysis/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── notebooks/
│ ├── 01_data_understanding.ipynb
│ ├── 02_data_cleaning.ipynb
│ └── 03_eda_analysis.ipynb
│
├── src/
│ ├── data_loader.py
│ ├── preprocessing.py
│ └── utils.py
│
├── visuals/
├── reports/
├── README.md
└── requirements.txt


---

## 🔄 Project Workflow

1. Data Collection & Loading  
2. Data Understanding  
3. Data Cleaning & Preprocessing  
4. Exploratory Data Analysis (EDA)  
5. Relationship Analysis (Glucose vs other variables)  
6. Insight Generation  
7. Predictive Modeling for glucose trends

---

## 📈 Key Objectives (to be updated during analysis)

- Identify patterns in glucose fluctuations
- Analyze impact of insulin dosage on glucose levels
- Study effect of carbohydrate intake on glucose spikes
- Understand relationship between physical activity and glucose control
- Explore time-based glucose trends
- Predictive modeling for glucose levels
- Hypoglycemia/hyperglycemia classification
- Time-series forecasting models
- Dashboard using Power BI / Streamlit

---

## 🚧 Current Status

- [x] Project structure setup
- [x] GitHub repository initialization
- [ ] Data loading and exploration
- [ ] Data cleaning
- [ ] Exploratory data analysis
- [ ] Insights and visualization
- [ ] Final report

---
### Final Model

Mention:

- Final model: Tuned Random Forest Regressor
- Evaluation metrics: MAE, RMSE, R²
- Main interpretation: recent glucose history was highly important for prediction

### Key Findings

Possible findings:

- Glucose values show meaningful variation across patients and time.
- Lag and rolling glucose features are strong predictors.
- Tuned Random Forest improved model performance compared with baseline models.
- Residual analysis showed where the model performed well and where errors remained.
- The model should not be used for clinical decision-making without further validation.

### Limitations

Mention:

- Limited patient sample
- Time-series dependency
- Possible patient-level generalization issues
- Missing real-world health factors
- Not clinically validated

---

## 🚀 How to Run This Project

Follow these steps to set up and run the project locally:

### 1. Clone the repository

git clone https://github.com/your-username/diabetes-glucose-analysis.git

### 2. Navigate to project folder
cd diabetes-glucose-analysis


### 3. Create virtual environment (optional but recommended)
python -m venv venv


### 4. Activate virtual environment

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

### 5. Install dependencies
pip install -r requirements.txt

### 6. Launch Jupyter Notebook
jupyter notebook

Then open:

notebooks/01_data_understanding.ipynb

Note: Trained model `.pkl` files are not included in this repository because they exceed GitHub file size limits. The model can be regenerated by running the notebooks in sequence.

## 👤 Author

- Name: *Humera Anjum*
- GitHub: *your-github-profile-link*

---

## 📜 License

This project is for educational and research purposes only.

