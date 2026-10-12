score = int(input("Введите балл (0-100): "))

if 90 <= score <= 100:
    print("Оценка: A")
elif 80 <= score <= 89:
    print("Оценка: B")
elif 70 <= score <= 79:
    print("Оценка: C")
elif 60 <= score <= 69:
    print("Оценка: D")
elif 0 <= score < 60:
    print("Оценка: F")
else:
    print("Некорректный балл")