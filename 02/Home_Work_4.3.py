import random
elements = random.randint(3, 10)
lst = [random.randint(1, 9) for i in range(elements)]
print(lst)
list_2 = [lst[0], lst[2], lst[-2]]
print(list_2)
