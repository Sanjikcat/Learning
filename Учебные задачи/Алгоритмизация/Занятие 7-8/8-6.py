weight = float(input("Вес (кг): "))
distance = float(input("Расстояние (км): "))

base_cost = 500
if weight > 5:
    base_cost += 300
if distance > 100:
    base_cost += 500

print(f"Стоимость доставки: {base_cost} тенге")