ticket = input("Введите 6-значный номер билета: ")

if len(ticket) == 6 and ticket.isdigit():
    sum1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    sum2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
    if sum1 == sum2:
        print("Билет счастливый!")
    else:
        print("Билет обычный")
else:
    print("Ошибка: введите ровно 6 цифр")