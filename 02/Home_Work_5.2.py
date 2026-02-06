# Модифікувати калькулятор
while True:
    try:
        n_1 = float(input('Введіть перше число: '))
        operator = input('Введіть дію: ').strip()
        n_2 = float(input('Введіть друге число: '))
        if operator == "+":
            print(n_1 + n_2)
        elif operator == "-":
            print(n_1 - n_2)
        elif operator == "*":
            print(n_1 * n_2)
        elif operator == "/":
            if n_2 == 0:
                print('Ділення на нуль неможливе')
            else:
                print(n_1 / n_2)
        else:
            print('Оператор введено з помилкою')
    except ValueError:
        print("Помилка: введіть числове значення!")
    c = input('Для продовження натисніть "y"').strip().lower()
    if c not in ['y', 'у']:
        print('Робота завершена')
        break
