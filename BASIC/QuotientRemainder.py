amtgive = int(input("Enter the amount to give: "))
billamt = int(input("Enter the bill amount: "))

if billamt == 0:
    print("Error: Cannot divide by zero")
else:
    quotient = amtgive // billamt  # Integer division for quotient
    remainder = amtgive % billamt  # Modulo for remainder
    print(f"Quotient:{quotient}")
    print(f"Remainder:{remainder}")
