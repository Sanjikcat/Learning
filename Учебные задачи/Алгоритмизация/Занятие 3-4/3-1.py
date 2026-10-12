a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

print(f"Сумма: {a + b}")
print(f"Разность: {a - b}")
print(f"Произведение: {a * b}")
print(f"Частное: {a / b if b != 0 else 'На ноль делить нельзя'}")