import math

r = float(input("Введите радиус: "))
area = math.pi * (r ** 2)
length = 2 * math.pi * r

print(f"Площадь: {area:.2f}")
print(f"Длина окружности: {length:.2f}")