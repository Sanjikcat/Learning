day = int(input("Введите день (1-31): "))
month = int(input("Введите месяц (1-12): "))

if 1 <= day <= 31 and 1 <= month <= 12:
    print("Дата корректна по базовым границам")
else:
    print("Ошибка в дате")