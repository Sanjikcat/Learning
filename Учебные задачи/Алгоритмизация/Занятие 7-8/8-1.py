income = float(input("Введите доход: "))

if income <= 50000:
    tax = income * 0.10
elif income <= 150000:
    tax = income * 0.15
else:
    tax = income * 0.20

print(f"Сумма налога: {tax}")