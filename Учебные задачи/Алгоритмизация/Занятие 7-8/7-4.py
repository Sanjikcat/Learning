correct_login = "admin"
correct_pass = "12345"

login = input("Введите логин: ")
password = input("Введите пароль: ")

if login == correct_login and password == correct_pass:
    print("Доступ разрешён")
else:
    print("Доступ запрещён")