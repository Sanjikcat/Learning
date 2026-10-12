number = input("Введите трёхзначное число: ")

if len(number) == 3 and number[0] == number[2]:
    print("Число симметричное (первая и последняя цифры равны)")
else:
    print("Число несимметричное")