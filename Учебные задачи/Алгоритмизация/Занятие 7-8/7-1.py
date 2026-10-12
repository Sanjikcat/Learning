a = float(input("Первое число: "))
op = input("Операция (+, -, *, /): ")
b = float(input("Второе число: "))

if op == "+":
    print(f"Результат: {a + b}")
elif op == "-":
    print(f"Результат: {a - b}")
elif op == "*":
    print(f"Результат: {a * b}")
elif op == "/":
    if b != 0:
        print(f"Результат: {a / b}")
    else:
        print("Ошибка: деление на ноль")
else:
    print("Неизвестная операция")