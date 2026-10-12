usd = float(input("Сумма в USD: "))
eur = float(input("Сумма в EUR: "))
rub = float(input("Сумма в RUB: "))

usd_rate = float(input("Курс USD к KZT: "))
eur_rate = float(input("Курс EUR к KZT: "))
rub_rate = float(input("Курс RUB к KZT: "))

print(f"USD в KZT: {usd * usd_rate}")
print(f"EUR в KZT: {eur * eur_rate}")
print(f"RUB в KZT: {rub * rub_rate}")