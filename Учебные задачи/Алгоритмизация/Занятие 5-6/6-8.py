score = int(input("Введите балл (0-100): "))

if 90 <= score <= 100:
    print("Уровень: A")
elif 80 <= score <= 89:
    print("Уровень: B")
elif 70 <= score <= 79:
    print("Уровень: C")
elif 60 <= score <= 69:
    print("Уровень: D")
else:
    print("Уровень: F (ниже 60)")