# Generate 500-row Customer Churn CSV
import pandas as pd
import numpy as np

np.random.seed(42)

n = 500

data = pd.DataFrame({
    "CustomerID": range(1, n+1),
    "Age": np.random.randint(18, 60, n),
    "Gender": np.random.choice(["Male", "Female"], n),
    "MonthlyCharge": np.random.randint(250000, 750000, n),
    "ContractType": np.random.choice(["Month-to-month", "One year", "Two year"], n, p=[0.5, 0.3, 0.2]),
    "InternetService": np.random.choice(["Fiber", "DSL"], n, p=[0.6, 0.4]),
    "Tenure": np.random.randint(1, 60, n),
})

# Create churn probability logic (higher for month-to-month & low tenure)
churn_prob = (
    (data["ContractType"] == "Month-to-month") * 0.4 +
    (data["Tenure"] < 12) * 0.3 +
    (data["MonthlyCharge"] > 600000) * 0.2 +
    0.1
)

data["Churn"] = np.where(np.random.rand(n) < churn_prob, "Yes", "No")

file_path = "/mnt/data/customer_churn_500_rows.csv"
data.to_csv(file_path, index=False)

file_path
