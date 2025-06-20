#Filter employees in the IT department with more than 5 years of experience and a salary above 70,000:
# Create the DataFrame
import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'IT'],
    'Salary': [80000, 50000, 90000, 75000, 65000],
    'Years_Experience': [6, 3, 7, 10, 4]
}
df = pd.DataFrame(data)

# Filter the DataFrame
filtered_employees = df[
    (df['Department'] == 'IT') & 
    (df['Years_Experience'] > 5) & 
    (df['Salary'] > 70000)
]

print("Filtered DataFrame (IT Department, Salary > 70,000, Years_Experience > 5):")
print(filtered_employees)
