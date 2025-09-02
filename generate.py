import pandas as pd
import random

def generate_loan_data(n=100):
    education_levels = ['High School', 'Bachelor', 'Master', 'PhD']
    data = []

    for _ in range(n):
        age = random.randint(21, 60)
        income = random.randint(20000, 150000)
        education = random.choice(education_levels)
        credit_score = random.randint(300, 850)
        loan_amount = random.randint(50000, 500000)

        # Simple rule-based approval logic
        approved = int((income > 40000 and credit_score > 650 and loan_amount < income * 5))

        data.append([age, income, education, credit_score, loan_amount, approved])

    df = pd.DataFrame(data, columns=['Age', 'Income', 'Education', 'CreditScore', 'LoanAmount', 'LoanApproved'])
    df.to_csv('data/loan_data.csv', index=False)

generate_loan_data()
