category = int(input("Введите категорию товара (1, 2 или 3): "))
price = float(input("Введите цену товара: "))

if category == 1:
    discount = 0.05
elif category == 2:
    discount = 0.10
elif category == 3:
    discount = 0.15
else:
    discount = 0.0

final_price = price * (1 - discount)
print(f"Скидка: {int(discount * 100)}%, Итоговая цена: {final_price}")