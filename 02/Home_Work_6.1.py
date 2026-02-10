# Написати програму, яка повертатиме всі символи між буквами
import string
user_input = input("Введіть дві літери через дефіс ")
alphabet = string.ascii_letters
first_letter, last_letter = user_input[0], user_input[-1]
index_1 = alphabet.index(first_letter)
index_2 = alphabet.index(last_letter)
result = alphabet[index_1:index_2 + 1]
print(result)
