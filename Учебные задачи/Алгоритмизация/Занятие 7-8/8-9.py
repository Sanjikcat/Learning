code = int(input("Введите защитный код: "))

if code == 111:
    print("Доступ: guest")
elif code == 222:
    print("Доступ: user")
elif code == 333:
    print("Доступ: admin")
else:
    print("Неверный код доступа")