password = input("Введите пароль: ")
has_digit = any(c.isdigit() for c in password)
has_upper = any(c.isupper() for c in password)

if len(password) >= 8 and has_digit and has_upper:
    print("Сложность: Сильный пароль")
elif len(password) >= 6 and has_digit:
    print("Сложность: Средний пароль")
else:
    print("Сложность: Слабый пароль")