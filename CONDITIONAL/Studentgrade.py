# Taking input from the user
grade = float(input("Enter the student's grade: "))
attendance = float(input("Enter the student's attendance percentage: "))

# Categorizing the student based on grade and attendance
if grade >= 90:
    if attendance >= 95:
        category = "Excellent"
    else:
        category = "Very Good"
elif 75 <= grade <= 89:
    if attendance >= 85:
        category = "Good"
    else:
        category = "Average"
elif 50 <= grade <= 74:
    category = "Pass"
else:
    category = "Fail"

# Outputting the result
print(f"The student is categorized as: {category}")
