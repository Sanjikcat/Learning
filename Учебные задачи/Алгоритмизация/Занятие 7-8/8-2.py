weight = float(input("Масса (кг): "))
height = float(input("Рост (м): "))
bmi = weight / (height ** 2)

print(f"Ваш ИМТ: {bmi:.2f}")
if 18.5 <= bmi <= 25:
    print("Вес в норме")
elif bmi < 18.5:
    print("Недостаток веса")
else:
    print("Избыток веса")