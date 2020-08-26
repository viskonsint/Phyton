a = int(input("Количество километров в первый день "))
b = int(input("Общее количество километров "))
days = 1
kilometres = a
while kilometres < b:
        a = a + 0.1 * a
        days += 1
        kilometres = kilometres + a
print(f"Вам осталось тренироваться %.d дней" % days)