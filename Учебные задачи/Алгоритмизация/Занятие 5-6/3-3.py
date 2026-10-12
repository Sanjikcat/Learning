weight = float(input("Введите массу (кг): "))
height = float(input("Введите рост (м): "))
bmi = weight / (height ** 2)
print(f"ИМТ: {bmi:.2f}")