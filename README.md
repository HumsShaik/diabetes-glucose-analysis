✍️  README.md

# 🩺 Project Title - Diabetes Glucose Analysis and Prediction

## 📌 Project Overview

This project analyzes diabetes glucose monitoring data using Python, exploratory data analysis, feature engineering, machine learning, and dashboard development.

The goal of this project is to understand glucose patterns across patients and build a machine learning model that can predict glucose levels using activity, insulin, carbohydrate, time-based, lag, and rolling glucose features.

The project follows a complete data analysis workflow, from raw data understanding to preprocessing, exploratory analysis, feature engineering, baseline modeling, hyperparameter tuning, final evaluation, and Streamlit dashboard creation.

---

## 🎯 Problem Statement

Managing Type 1 Diabetes requires maintaining stable blood glucose levels. However, glucose fluctuations are influenced by multiple factors such as insulin dosage, carbohydrate intake, physical activity, and physiological signals. Understanding these relationships is essential for improving diabetes management and reducing risks of hypoglycemia and hyperglycemia.

---

## 🧠 Business / Research Goal

Diabetes management depends heavily on understanding glucose behavior over time. This project aims to:

- Analyze glucose trends across multiple patients
- Identify patterns related to time, activity, insulin, carbohydrates, and previous glucose values
- Build regression models to predict glucose values
- Evaluate model performance using multiple validation strategies
- Present final insights through a Streamlit dashboard

---

## 📊 Dataset Information

This project uses the **HUPA-UCM Diabetes Dataset**, which contains Continuous Glucose Monitoring (CGM) data and wearable sensor data collected from 25 individuals with Type 1 Diabetes Mellitus (T1DM).

The dataset contains patient-level time-series records with features such as:

- Glucose
- Calories
- Heart rate
- Steps
- Basal insulin rate
- Bolus insulin volume
- Carbohydrate input
- Timestamp-based features
- Lag glucose features
- Rolling glucose features

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

## 📁 Project Structure

```text
diabetes-glucose-analysis/
│
├── data/
│   ├── raw/
│   ├── processed/
│   │   ├── diabetes_glucose_processed.csv
│   │   ├── patient_summary.csv
│   │   ├── modeling_ready_dataset.csv
│   │   └── modeling_feature_list.csv
│
├── models/
│   ├── best_baseline_model.pkl
│   └── final_tuned_random_forest_model.pkl
│
├── outputs/
│   ├── baseline_model_results.csv
│   ├── baseline_best_model_predictions.csv
│   ├── baseline_model_feature_list.csv
│   ├── tuned_model_results.csv
│   ├── tuned_model_predictions.csv
│   └── tuned_model_feature_list.csv
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning_preprocessing.ipynb
│   ├── 03_exploratory_data_analysis.ipynb
│   ├── 04_feature_analysis_modeling_preparation.ipynb
│   ├── 05_baseline_modeling.ipynb
│   └── 06_model_improvement_hyperparameter_tuning.ipynb
│
├── dashboard/
│   └── app.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## 🔄 Project Workflow

### 1. Data Understanding

The first notebook explored the structure, columns, data types, patient files, timestamp range, and initial data quality.

### 2. Data Cleaning and Preprocessing

The second notebook combined multiple patient files, created patient IDs, converted timestamps, handled missing values, checked duplicates, validated time intervals, created glucose categories, and saved processed datasets.

### 3. Exploratory Data Analysis

The third notebook analyzed glucose distributions, glucose categories, patient-level trends, time-based glucose behavior, and relationships between glucose and other health/activity variables.

### 4. Feature Analysis and Modeling Preparation

The fourth notebook prepared the modeling dataset, selected useful features, analyzed correlations, created lag and rolling features, and saved the final modeling-ready files.

### 5. Baseline Modeling

The fifth notebook trained baseline regression models including:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

Models were evaluated using:

- Mean Absolute Error
- Root Mean Squared Error
- R² Score

Different split strategies were tested:

- Random split
- Chronological split
- Patient-level split

### 6. Model Improvement and Hyperparameter Tuning

The sixth notebook improved the best baseline model using hyperparameter tuning. A tuned Random Forest model was selected as the final model based on performance and interpretability.

### 7. Streamlit Dashboard

A Streamlit dashboard was created to present:

- Project overview
- Final model metrics
- Actual vs predicted glucose values
- Residual analysis
- Feature importance
- Model limitations
- Final conclusions

---

## Final Model

Final model: Tuned Random Forest Regressor
Evaluation metrics: MAE, RMSE, R²
Main interpretation: recent glucose history was highly important for prediction

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

## 🛠️ Tools & Technologies Used

- Python 🐍
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Git
- GitHub
- Jupyter Notebook

---

## 🚀 How to Run This Project

Follow these steps to set up and run the project locally:

### 1. Clone the repository

git clone https://github.com/HumsShaik/diabetes-glucose-analysis.git

### 2. Navigate to project folder
cd diabetes-glucose-analysis


### 3. Create virtual environment (optional but recommended)
python -m venv venv


### 4. Activate virtual environment

For Windows PowerShell:

venv\Scripts\Activate.ps1

For Command Prompt:

venv\Scripts\activate

### 5. Install dependencies
pip install -r requirements.txt

### 6. Launch Jupyter Notebook

Then open:

notebooks/01_data_understanding.ipynb

### 7. Run the Streamlit dashboard

streamlit run dashboard/app.py

---

## Final Project Review Checklist

Before publishing this project to GitHub, the following checks were completed:

- All notebooks run from top to bottom without errors
- Notebook outputs were reviewed and cleaned
- Final datasets were saved in the correct folders
- Baseline and tuned model results were saved
- Final model predictions were saved
- Final trained model file was saved
- Feature list was saved
- README was updated with project goal, workflow, findings, limitations, and future work
- Repository folders were organized professionally
- requirements.txt was prepared
- .gitignore was prepared
- Streamlit dashboard was created
- Final GitHub push was completed
Note: Trained model `.pkl` files are not included in this repository because they exceed GitHub file size limits. The model can be regenerated by running the notebooks in sequence.
---

## Final Project Summary

This project demonstrates a complete end-to-end data analysis and machine learning workflow using diabetes glucose monitoring data. The project begins with raw patient-level time-series data and progresses through data understanding, cleaning, preprocessing, exploratory data analysis, feature engineering, baseline modeling, hyperparameter tuning, model evaluation, and dashboard creation.
The final tuned Random Forest model predicts glucose levels using health, activity, insulin, carbohydrate, time-based, lag, and rolling glucose features. The project also includes a Streamlit dashboard to communicate model results, prediction performance, residual patterns, feature importance, limitations, and conclusions in an interactive format.

---

### Key Findings

- Lag glucose features were highly important, showing that recent glucose history is strongly related to near-future glucose levels.
- Rolling glucose features improved model performance by capturing short-term glucose trends.
- Time-based features helped identify daily glucose patterns.
- Random Forest performed better than linear regression and decision tree baseline models.
- Patient-level evaluation showed that glucose prediction is more difficult when testing on patients not seen during training.
- The final model provides useful predictive insights, but it should not be used for medical decisions.

---

### Limitations

- The dataset contains a limited number of patients.
- Patient behavior and glucose response can vary significantly.
- Important real-world factors such as sleep, stress, illness, meal composition, and medication timing were not fully captured.
- The model depends heavily on recent glucose history, which may limit usefulness when glucose lag data is unavailable.
- Random train-test splits may overestimate performance because time-series observations close together can be very similar.
- The model is intended for educational and analytical purposes only.
---

## Future Work

Future improvements could include:

- Build patient-specific models
- Add advanced time-series validation
- Compare additional algorithms such as XGBoost, LightGBM, and LSTM models
- Include more patient data
- Add model explainability using SHAP
- Deploy the Streamlit dashboard online
- Create a Power BI dashboard version
- Add interactive patient-level filtering
- Add prediction confidence intervals
---


## 👤 Author

- Name: *Humera Anjum*
- GitHub: *https://github.com/HumsShaik*

---

## Streamlit Dashboard Link

https://diabetes-glucose-analysis.streamlit.app/

---

## 📜 License

This project is for educational and research purposes only.

