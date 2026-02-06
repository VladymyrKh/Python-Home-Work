import string
import keyword

word = input("Введіть дані")
first_check = word[0].isdigit() if word else False
second_check = any(i.isupper() for i in word)
rep = string.punctuation.replace('_', '') + ' '
third_check = any(i in rep for i in word)
fourth_check = '__' in word
fifth_check = word in keyword.kwlist
sixth_check = len(word) == 0
if (first_check or second_check or third_check or
        fourth_check or fifth_check or sixth_check):
    print(False)
else:
    print(True)
