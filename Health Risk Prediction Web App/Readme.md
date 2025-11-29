# Health Risk Prediction Web App  
**Python · Pandas · Machine Learning · Flask API · Google Colab**

This project is a machine learning–powered web application designed to predict the likelihood of three common health risks:

- **High Blood Pressure**  
- **Diabetes**  
- **Anxiety Disorders**

The system uses cleaned and standardized health datasets, trains individual machine learning models for each condition, and exposes predictions through a RESTful Flask API.

---

## Dataset  
**Source:** Course-provided dataset (synthetic health survey data)  
**Format:** CSV  
**Tools Used:** Google Colab, Pandas  

The dataset included a variety of health and lifestyle variables such as:

- Age  
- BMI  
- Exercise frequency  
- Stress level  
- Smoking/alcohol use  
- Sleep patterns  
- Nutrition indicators  

---

## Data Cleaning & Preparation

All preprocessing was performed using **Pandas** in Google Colab.  
Key steps included:

### Removing null values  
Handled using `.dropna()` and selective imputation where appropriate.

### Standardizing column names  
Converted to lowercase, replaced spaces with underscores.

### Selecting relevant features  
Variables with meaningful predictive value were kept; redundant or low-signal columns removed.

### Creating condition-specific datasets  
Three separate datasets were prepared — one for each condition (blood pressure, diabetes, anxiety), each with its own target label.

---

## Machine Learning Model

Each condition uses its own ML model trained on the prepared subsets.

- Models were trained in **Google Colab**  
- Evaluation metrics were exported (accuracy, precision, recall)  
- Algorithms used (based on Canvas project requirements):  
  - Logistic Regression  
  - Decision Tree / Random Forest  
  - SVM (optional depending on file)

These models served as the core prediction engines for the API.

---

## Flask API Integration

A lightweight REST API was built using **Flask** to deliver real-time predictions.

### **API Workflow**
1. Receive JSON input (e.g., age, BMI, stress level, etc.)  
2. Convert input into model-ready format  
3. Run prediction through the condition-specific model  
4. Return prediction as JSON response

---

## Sample Input (JSON)

```json
{
  "age": 42,
  "bmi": 28.5,
  "exercise_frequency": 3,
  "stress_level": 4,
  "sleep_hours": 6
}

