# Для списку цілих чисел потрібно знайти суму елементів із парними індексами
my_list = []
if len(my_list) > 0:
    total = sum(my_list[::2]) * my_list[-1]
    print(total)
else:
    print(len(my_list))
