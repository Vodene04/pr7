def uravnenie():
    try:
        a = int(input("Введите значение a: "))
        b = int(input("Введите значение b: "))
        c = int(input("Введите значение c: "))
#Формула уравнения
        x = a + b * 4 - c
#Вывод результата
        print(f"Результат уравнения {x}")
    except ValueError:
        print("Ошибка")
uravnenie()