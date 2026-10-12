celsius = float(input("Введите температуру в Цельсиях: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

fahr_input = float(input("Введите температуру в Фаренгейтах: "))
cels_output = (fahr_input - 32) * 5/9
print(f"{fahr_input}°F = {cels_output:.2f}°C")