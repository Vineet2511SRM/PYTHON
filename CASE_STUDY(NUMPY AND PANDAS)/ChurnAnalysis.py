import pandas as pd
import numpy as np

# Sample dataset
data = {
    'CustomerID': [101, 102, 103, 104, 105, 106],
    'Gender': ['Male', 'Female', 'Female', 'Male', None, 'Female'],
    'Age': [25, 35, np.nan, 45, 50, 29],
    'Tenure': [12, 24, 5, np.nan, 60, 18],
    'MonthlyCharges': [30.5, 40.7, 20.3, 35.5, np.nan, 28.6],
    'TotalCharges': [365, 960, 101, 425, 2100, 514],
    'Churn': ['No', 'Yes', 'Yes', 'No', 'No', 'Yes']
}

# Create a DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Handle missing values
df['Gender'] = df['Gender'].fillna('Unknown')  # Avoid in-place modification
df['Age'] = df['Age'].fillna(np.mean(df['Age']))
df['Tenure'] = df['Tenure'].fillna(0)
df['MonthlyCharges'] = df['MonthlyCharges'].fillna(np.mean(df['MonthlyCharges']))

print("\nCleaned DataFrame:\n", df)

# Basic statistics using Pandas
print("\nDescriptive Statistics (Pandas):\n", df.describe())

# Calculate statistics using NumPy
mean_age = np.mean(df['Age'])
median_tenure = np.median(df['Tenure'])
std_monthly_charges = np.std(df['MonthlyCharges'])

print("\nStatistics using NumPy:")
print(f"Mean Age: {mean_age}")
print(f"Median Tenure: {median_tenure}")
print(f"Standard Deviation of Monthly Charges: {std_monthly_charges}")

# Calculate churn rate using Pandas
churn_rate = df['Churn'].value_counts(normalize=True, dropna=False) * 100  # Ensures NaN are handled properly
print("\nChurn Rate:\n", churn_rate)

# NumPy example: Calculate churn percentage manually
churn_values = np.array(df['Churn'] == 'Yes', dtype=int)
churn_percentage = np.mean(churn_values) * 100
print("\nChurn Percentage (NumPy): {:.2f}%".format(churn_percentage))

# Pandas GroupBy example
gender_churn = df.groupby('Gender')['Churn'].value_counts(normalize=True, dropna=False).unstack()
print("\nGender-Wise Churn Rates:\n", gender_churn)

# NumPy example: Gender-wise count of churn
male_churn = np.sum((df['Gender'] == 'Male') & (df['Churn'] == 'Yes'))
female_churn = np.sum((df['Gender'] == 'Female') & (df['Churn'] == 'Yes'))

print("\nChurn Count (NumPy):")
print(f"Male Churn Count: {male_churn}")
print(f"Female Churn Count: {female_churn}")

# Correlation matrix using NumPy
numerical_data = df[['Age', 'Tenure', 'MonthlyCharges', 'TotalCharges']].values  # Use .values for a clearer NumPy array

# Calculate correlations
correlation_matrix = np.corrcoef(numerical_data.T)  # Transpose for correlation calculation
print("\nCorrelation Matrix (NumPy):\n", correlation_matrix)

# Corresponding column names
columns = ['Age', 'Tenure', 'MonthlyCharges', 'TotalCharges']
print("\nColumns for Correlation Matrix:", columns)
