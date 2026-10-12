years = int(input("Введите стаж работы (лет): "))

if 1 <= years < 3:
    print("Бонус: 5%")
elif 3 <= years < 5:
    print("Бонус: 10%")
elif years >= 5:
    print("Бонус: 20%")
else:
    print("Бонусов нет")