number = input("Введите целое число в десятичной системе: ")
#Проверка на то, является ли ввод с клавиатуры целым числом
if number.lstrip('-').isdigit():
    number = int(number)
#Случай для 0 и полож. чисел
    if number >= 0:
        bin = bin(number)[2:]
        oct = oct(number)[2:]
#Случай для отриц. чисел
    else:
        bin = '-' + bin(number)[3:]
        oct = '-' + oct(number)[3:]
    print(f"Двоичное представление: {bin}")
    print(f"Восьмеричное представление: {oct}")
else:
    print("Ошибка ввода!.")