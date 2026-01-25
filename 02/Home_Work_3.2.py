# Перенести останній елемент списку з кінця на початок
list_a = [12, 3, 4, 10]
if len(list_a) > 1:
    list_b = list_a[-1:] + list_a[:-1]
    print("Ваш результат", list_b)
else:
    print(list_a)
print("End")
