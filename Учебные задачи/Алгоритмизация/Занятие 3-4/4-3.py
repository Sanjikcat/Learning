birth_year = int(input("Год рождения: "))
current_year = 2026
age_years = current_year - birth_year

days = age_years * 365
hours = days * 24
minutes = hours * 60

print(f"Дней: {days}, Часов: {hours}, Минут: {minutes}")