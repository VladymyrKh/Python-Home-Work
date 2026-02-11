user_input = input("Введіть число ")
if user_input.isdigit():
    f = int(user_input)
    while f > 9:
        a = 1
        for i in str(f):
            a *= int(i)
        f = a
    print("Ваш результат = ", f)
else:
    print("Введіть коректне число")
