password = input("Введите пароль: ")
has_digit = any(char.isdigit() for char in password)

if len(password) >= 8 and has_digit:
    print("Пароль надежный")
else:
    print("Пароль не соответствует требованиям (нужно >= 8 символов и наличие цифр)")