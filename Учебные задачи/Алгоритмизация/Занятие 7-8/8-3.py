place = int(input("Введите ваше место в рейтинге: "))

if 1 <= place <= 3:
    print("Призовое место!")
elif 4 <= place <= 10:
    print("Призёр!")
else:
    print("Участник")