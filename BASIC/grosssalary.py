# Input: Basic pay
basic_pay = float(input("Enter the basic pay of the employee: "))

# Check constraints
if 20000 <= basic_pay <= 75000:
    # Calculate HRA (80% of basic pay)
    hra = 0.80 * basic_pay
    # Calculate DA (40% of basic pay)
    da = 0.40 * basic_pay
    # Calculate gross salary
    gross_salary = basic_pay + hra + da
    # Print gross salary rounded to 2 decimal places
    print(f"Gross Salary: {round(gross_salary, 2)}")
else:
    print("Basic pay should be between 20000 and 75000.")
