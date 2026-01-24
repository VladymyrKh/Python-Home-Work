# Програма має виконувати прості математичні дії (+, -, *, /). Перевірити при діленні на нуль
number_1 = float(input("Введіть перше число"))
operation =input("Введіть математичну дію")
number_2 = float(input("Введіть друге число"))
if operation == "+":
    print("Результат=", number_1 + number_2)
elif operation == "-":
    print("Результат=", number_1 - number_2)
elif operation == "*":
    print("Результат=", number_1 * number_2)
elif operation == "/":
    if number_2 == 0:
        print("Ділення на нуль неможливе")
    else:
        print("Результат=", number_1 / number_2)
else:
    print("Дія незрозуміла. Перевірте дані")
print ("End")


