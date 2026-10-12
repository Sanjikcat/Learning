hour = int(input("Введите час (0-23): "))

if 6 <= hour <= 11:
    print("Утро")
elif 12 <= hour <= 17:
    print("День")
elif 18 <= hour <= 23:
    print("Вечер")
elif 0 <= hour <= 5:
    print("Ночь")
else:
    print("Некорректный час")