from src.preprocess import preprocess_data
from src.train_models import train_models
from src.evaluate import evaluate_model
from src.predict import predict_loan_approval

# Load and preprocess
X, y = preprocess_data('data/loan_data.csv')

# Train models
log_model, rf_model, X_test, y_test = train_models(X, y)

# Evaluate
evaluate_model(log_model, X_test, y_test, "Logistic Regression")
evaluate_model(rf_model, X_test, y_test, "Random Forest")

# Predict sample
sample_input = [35, 50000, 1, 700, 200000]  # Age, Income, Education, CreditScore, LoanAmount
print("Prediction (Logistic):", predict_loan_approval(log_model, sample_input))
print("Prediction (Random Forest):", predict_loan_approval(rf_model, sample_input))
