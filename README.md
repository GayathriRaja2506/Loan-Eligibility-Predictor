# Loan-Eligibility-Predictor

A machine learning project that predicts whether a loan application should be approved based on applicant details. This tool is designed for fintech mockups, educational demos, or internal loan assessment simulations.

---

## 🎯 Objective

Build a classification model to predict loan approval using applicant features such as age, income, education level, credit score, and loan amount.

---

## 📂 Project Structure

```
LoanEligibilityPredictor/
├── data/
│   └── loan_data.csv
├── src/
│   ├── preprocess.py
│   ├── train_models.py
│   ├── evaluate.py
│   └── predict.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

The dataset contains 100 synthetic records with the following columns:

- `Age`: Applicant's age
- `Income`: Monthly income
- `Education`: Categorical (High School, Bachelor, Master, PhD)
- `CreditScore`: Ranges from 300 to 850
- `LoanAmount`: Requested loan amount
- `LoanApproved`: Target variable (1 = Approved, 0 = Rejected)

You can generate the dataset using `generate_data.py` or manually place `loan_data.csv` in the `data/` folder.

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/LoanEligibilityPredictor.git
cd LoanEligibilityPredictor

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Running the App

```bash
python main.py
```

This script will:
- Preprocess the dataset
- Train Logistic Regression and Random Forest models
- Display confusion matrices and ROC curves
- Print sample predictions in the terminal

---

## 📈 Model Evaluation

Models are evaluated using:
- **Confusion Matrix**: Visualizes true vs predicted classifications
- **ROC Curve**: Measures model performance across thresholds
- **AUC Score**: Quantifies ROC performance

---

## 🔮 Sample Prediction

```python
sample_input = [35, 50000, 1, 700, 200000]  # Age, Income, Education, CreditScore, LoanAmount
```

Output:
```
Prediction (Logistic): Approved
Prediction (Random Forest): Approved
```

---

## 🧠 Technologies Used

- Python 3.8+
- pandas
- scikit-learn
- matplotlib
- seaborn
