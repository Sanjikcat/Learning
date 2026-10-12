a = float(input("Сторона A: "))
b = float(input("Сторона B: "))
c = float(input("Сторона C: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Равносторонний треугольник")
    elif a == b or b == c or a == c:
        print("Равнобедренный треугольник")
    else:
        print("Разносторонний треугольник")
else:
    print("Такой треугольник не существует")