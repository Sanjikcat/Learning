completed = input("План выполнен? (да/нет): ").lower()

if completed == "да":
    percent = 25
else:
    percent = 0

print(f"Ваша премия: {percent}%")