profit = float(input("Введите доходы фирмы "))
costs = float(input("Введите расходы фирмы "))
if profit > costs:
    print(f"Рентабельность выручки составила {profit / costs:.2f}")
    workers = int(input("Введите число работников"))
    print(f"Один сотрудник составляет доход фирмы {profit / workers:.2f}")