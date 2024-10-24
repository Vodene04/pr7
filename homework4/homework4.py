def uravnenie():
    try:
        a = int(input("Введите значение целое значение a: "))
        b = int(input("Введите значение целое значение b: "))
        c = int(input("Введите значение целое значение c: "))
        x = a + b * 4 - c
#Вывод результата
        print(f"Результат уравнения {x}")
    except ValueError:
        print("Ошибка")
uravnenie()