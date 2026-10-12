distance = float(input("Расстояние (км): "))
consumption = float(input("Расход топлива (л на 100 км): "))
price = float(input("Цена за 1 литр: "))

total_cost = (distance * consumption / 100) * price
print(f"Стоимость поездки: {total_cost}")