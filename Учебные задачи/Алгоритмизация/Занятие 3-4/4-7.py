bill = float(input("Сумма счёта: "))
tip_percent = float(input("Процент чаевых: "))
total = bill * (1 + tip_percent / 100)
print(f"Итого к оплате: {total}")