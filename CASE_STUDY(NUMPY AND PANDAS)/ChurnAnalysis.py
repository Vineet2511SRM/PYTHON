import pandas as pd
import numpy as np

# --------------------- Step 1: Create Sample Dataset ---------------------
data = {
    'CustomerID': [101, 102, 103, 104, 105, 106],
    'Gender': ['Male', 'Female', 'Female', 'Male', None, 'Female'],
    'Age': [25, 35, np.nan, 45, 50, 29],
    'Tenure': [12, 24, 5, np.nan, 60, 18],
    'MonthlyCharges': [30.5, 40.7, 20.3, 35.5, np.nan, 28.6],
    'TotalCharges': [365, 960, 101, 425, 2100, 514],
    'Churn': ['No', 'Yes', 'Yes', 'No', 'No', 'Yes']
}

df = pd.DataFrame(data)
print("📋 Original DataFrame:\n", df)

# --------------------- Step 2: Handle Missing Values ---------------------
df['Gender'] = df['Gender'].fillna('Unknown')
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Tenure'] = df['Tenure'].fillna(0)
df['MonthlyCharges'] = df['MonthlyCharges'].fillna(df['MonthlyCharges'].mean())

print("\n✅ Cleaned DataFrame:\n", df)

# --------------------- Step 3: Basic Statistics Using Pandas ---------------------
print("\n📊 Descriptive Statistics (Pandas):\n", df.describe())

# --------------------- Step 4: Statistics Using NumPy ---------------------
mean_age = np.mean(df['Age'])
median_tenure = np.median(df['Tenure'])
std_monthly_charges = np.std(df['MonthlyCharges'])

print("\n📈 Statistics using NumPy:")
print(f"• Mean Age: {mean_age:.2f}")
print(f"• Median Tenure: {median_tenure}")
print(f"• Std. Dev. of Monthly Charges: {std_monthly_charges:.2f}")

# --------------------- Step 5: Churn Analysis ---------------------
churn_rate = df['Churn'].value_counts(normalize=True) * 100
print("\n📉 Churn Rate (%):\n", churn_rate)

# Manual Churn % using NumPy
churn_array = np.array(df['Churn'] == 'Yes', dtype=int)
churn_percentage = np.mean(churn_array) * 100
print(f"\n🧮 Churn Percentage (NumPy): {churn_percentage:.2f}%")

# --------------------- Step 6: Gender-Wise Churn ---------------------
gender_churn = df.groupby('Gender')['Churn'].value_counts(normalize=True).unstack()
print("\n🚻 Gender-Wise Churn Rates:\n", gender_churn)

# NumPy alternative churn count
male_churn_count = np.sum((df['Gender'] == 'Male') & (df['Churn'] == 'Yes'))
female_churn_count = np.sum((df['Gender'] == 'Female') & (df['Churn'] == 'Yes'))

print("\n🔢 Churn Count (NumPy):")
print(f"• Male Churn Count: {male_churn_count}")
print(f"• Female Churn Count: {female_churn_count}")

# --------------------- Step 7: Correlation Matrix ---------------------
numerical_cols = ['Age', 'Tenure', 'MonthlyCharges', 'TotalCharges']
numerical_data = df[numerical_cols].values

correlation_matrix = np.corrcoef(numerical_data.T)

# Present as a DataFrame for better readability
corr_df = pd.DataFrame(correlation_matrix, index=numerical_cols, columns=numerical_cols)
print("\n🔗 Correlation Matrix:\n", corr_df.round(2))


#THE END 