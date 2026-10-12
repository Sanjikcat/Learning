a = float(input("Первое число: "))
b = float(input("Второе число: "))
c = float(input("Третье число: "))

max_num = a
if b > max_num:
    max_num = b
if c > max_num:
    max_num = c

print(f"Максимальное число: {max_num}")