day = int(input("День рождения: "))
month = int(input("Месяц рождения (1-12): "))

if (month == 3 and day >= 21) or (month == 4 and day <= 19):
    print("Овен")
elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
    print("Телец")
else:
    print("Другой знак зодиака (пример для демонстрации условных ветвлений)")