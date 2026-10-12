grades = [float(input(f"Оценка {i+1}: ")) for i in range(5)]
print(f"Среднее арифметическое: {sum(grades) / len(grades)}")