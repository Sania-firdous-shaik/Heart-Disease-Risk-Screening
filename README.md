# ❤️ Heart Disease Risk Screening
### A Hybrid Logistic Regression–Random Forest Model-Based Solution

## 📌 Project Overview

Heart disease is one of the major health concerns worldwide, making early risk identification an important step in preventive healthcare.

This project presents a machine learning-based approach for preliminary heart disease risk screening using the **Cleveland Heart Disease dataset**. It explores Logistic Regression and Random Forest models, along with a soft-voting ensemble, to classify patients into two categories based on the presence or absence of heart disease.

The trained model is integrated into an interactive Streamlit application where users can enter patient health parameters and receive a model-generated risk assessment.

The project demonstrates how machine learning can support accessible, data-driven preliminary screening.

## 🎯 Objectives

- Develop a machine learning pipeline for heart disease risk classification.
- Explore Logistic Regression and Random Forest algorithms.
- Implement a soft-voting ensemble to combine model predictions.
- Perform data preprocessing and feature engineering.
- Evaluate model performance using classification metrics and cross-validation.
- Build an interactive web application for risk screening.

## 🗂️ Dataset

**Dataset:** Cleveland Heart Disease Dataset

- Original dataset size: 303 records
- Number of attributes: 14, including the target variable
- Problem type: Binary Classification

### Features

| Feature | Description |
|---|---|
| age | Age of the patient |
| sex | Sex category |
| cp | Chest pain type |
| trestbps | Resting blood pressure |
| chol | Serum cholesterol |
| fbs | Fasting blood sugar |
| restecg | Resting electrocardiographic results |
| thalach | Maximum heart rate achieved |
| exang | Exercise-induced angina |
| oldpeak | ST depression |
| slope | Slope of peak exercise ST segment |
| ca | Number of major vessels |
| thal | Thalassemia category |
| target | Heart disease indicator |

### Target Variable

The original target is converted into a binary classification variable:

- `0` – No heart disease
- `1` – Heart disease present

## ⚙️ Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Algorithms | Logistic Regression, Random Forest |
| Ensemble Learning | Soft Voting Classifier |
| Model Interpretation | SHAP |
| Visualization | Matplotlib, Seaborn |
| Web Framework | Streamlit |
| Model Serialization | Joblib |
| Deployment | Render |
| Development Environment | Jupyter Notebook, VS Code |

## 🔬 Methodology

The project follows a structured machine learning workflow.

### 1. Data Preprocessing

- Loaded the Cleveland Heart Disease dataset.
- Converted the original target into a binary classification variable.
- Handled missing values using appropriate imputation strategies.
- Applied numerical feature scaling.
- Encoded categorical features using One-Hot Encoding.

### 2. Feature Engineering

Two additional features were created to explore relationships between patient attributes:

- `chol_per_age` = Cholesterol / Age
- `bps_per_age` = Resting Blood Pressure / Age

### 3. Model Development

The following machine learning models were developed and evaluated:

**Logistic Regression**

A classification algorithm used to estimate the likelihood of a binary outcome based on input features.

**Random Forest**

An ensemble learning algorithm that combines multiple decision trees to improve classification performance.

**Soft Voting Classifier**

Combines predicted class probabilities from multiple models to generate an ensemble prediction.

**XGBoost (Optional Model)**

An additional gradient-boosting model was explored for performance comparison.

### 4. Model Evaluation

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Repeated Stratified 5-Fold Cross-Validation

The final model was selected based on repeated cross-validation ROC-AUC performance.

## 📊 Model Performance

### Repeated Cross-Validation Results

The following results were obtained using repeated 5-fold cross-validation with 5 repeats.

| Model | Mean ROC-AUC |
|---|---:|
| Logistic Regression | 0.8971 |
| Random Forest | 0.8932 |
| Soft Voting Ensemble | 0.8921 |
| XGBoost | 0.8722 |

**Selected Model: Logistic Regression**

Logistic Regression achieved the highest mean cross-validation ROC-AUC among the evaluated models and was selected as the final model.

### Holdout Test Results

| Evaluation Metric | Score |
|---|---:|
| Accuracy | 88.52% |
| Precision | 83.87% |
| Recall | 92.86% |
| F1-Score | 88.14% |
| ROC-AUC | 96.54% |

*Note: These are experimental results from the notebook's evaluation. Performance on other datasets or real-world patient populations may differ.*

## 🖥️ Application Features

The project includes an interactive Streamlit application.

- Patient health parameter input form.
- Machine learning-based risk classification.
- Model-generated positive-class score.
- Interactive risk assessment interface.
- Model performance overview.
- Evaluation metric visualization.
- Educational disclaimer.

## 📁 Project Structure

```text
Heart-Disease-Risk-Screening/
│
├── app.py
│
├── heart_disease_model.joblib
│
├── Heart_disease_cleveland_new.csv
│
├── Interpretable Machine Learning for Heart Diseases Prediction.ipynb
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

## 🚀 Installation and Setup

### Prerequisites

- Python 3.9 or later
- Git
- pip

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Heart-Disease-Risk-Screening.git
```

### Step 2: Navigate to the Project Directory

```bash
cd Heart-Disease-Risk-Screening
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## ☁️ Deployment

The application can be deployed using Render.

**Deployment configuration:**

| Setting | Value |
|---|---|
| Environment | Python |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `streamlit run app.py --server.port $PORT --server.address 0.0.0.0` |

After deployment, the application can be accessed through its public Render URL.

## 🔍 Model Interpretation

SHAP (SHapley Additive exPlanations) was explored to understand feature contributions to model predictions.

This provides insights into how individual input features influence the model's output and supports model interpretability.

## ⚠️ Limitations and Disclaimer

- This project is developed for academic, educational, and research purposes.
- The model is trained using a relatively small Cleveland Heart Disease dataset.
- Its predictions are not a substitute for professional medical evaluation.
- The displayed model score is not a clinically validated probability of developing heart disease.
- The system should not be used for medical diagnosis or treatment decisions.

## 🔮 Future Enhancements

- Evaluate the model using larger and more diverse datasets.
- Perform external validation on independent patient data.
- Improve model interpretability through additional explainability techniques.
- Explore hyperparameter optimization.
- Enhance the user interface and accessibility.
- Investigate further ensemble strategies and calibration methods.

## 👩‍💻 Author

**Sania Firdous Shaik**

B.Tech – Artificial Intelligence and Data Science

GitHub: [Saniafirdous-shaik](https://github.com/Saniafirdous-shaik)

LinkedIn: [Sania Firdous Shaik](https://linkedin.com/in/sania-firdous-shaik/)

---

⭐ If you find this project interesting, consider giving the repository a star!

**Disclaimer:** This application is intended for preliminary educational screening and is not a clinically validated medical tool.
