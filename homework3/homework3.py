#Функция преобразования в 5-ричную систему
def preobrazovanie(n):
    if n < 5:
        return str(n)
    else:
        return preobrazovanie(n // 5) + str(n % 5)
    
number = input("Введите целое положительное число ")
#Проверка на правильность ввода
if number.isdigit():
    number = int(number)
    print(f"Представление в 5-ричной системе: {preobrazovanie(number)}")
else:
    print("Ошибка!")