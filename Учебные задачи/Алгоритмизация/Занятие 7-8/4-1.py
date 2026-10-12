price = float(input("Цена за единицу: "))
qty = int(input("Количество: "))

total = price * qty
discounted = total * 0.9
print(f"Сумма со скидкой 10%: {discounted}")