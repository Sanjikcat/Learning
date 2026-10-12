total = float(input("Сумма покупки: "))

if total < 10000:
    discount = 0
elif total < 50000:
    discount = 5
elif total < 100000:
    discount = 10
else:
    discount = 15

final = total * (1 - discount / 100)
print(f"Скидка: {discount}%, К оплате: {final}")