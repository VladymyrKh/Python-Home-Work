# Розділити один список на два та помістити їх у новий список.

list = [1, 2, 3, 4, 5]
list_length = (len(list) + 1) // 2
list_1 = list[:list_length]
list_2 = list[list_length:]

print([list_1, list_2])
