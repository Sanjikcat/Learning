# Упрощенная логика по аналогии с размерами A-форматов
format_type = input("Введите формат (A4, A3, A2): ").upper()

if format_type == "A4":
    print("Размер: 210 x 297 мм")
elif format_type == "A3":
    print("Размер: 297 x 420 мм")
elif format_type == "A2":
    print("Размер: 420 x 594 мм")
else:
    print("Неизвестный формат")