import math
#Користувач вводить число. Програма виводить його квадрат.
number_1=int(input("Введіть число="))
res_1=number_1**2
print("Результат=",res_1)

#Програма запитує три числа і виводить їх середнє арифметичне.
num_1=int(input("Перше число="))
num_2=int(input("Друге число="))
num_3=int(input("Третє число="))
res_2=float((num_1+num_2+num_3)/3)
print('Середнє арефметичне значення=',res_2)

#Користувач вводить кількість хвилин. Програма виводить, скільки це годин і хвилин.
total_minute = int(input("Введіть кількість хвилин="))
h = total_minute//60
m = total_minute%60
print(h,"години",m,"хвилин")

#Користувач вводить ціну товару і розмір знижки у %.
price = float(input("Введіть ціну товара"))
discount_percent = float(input("Введіть знижку (%)"))
discount_amount = (price * discount_percent) / 100
final_price = price - discount_amount
print("Кінцева ціна=", final_price)

#Користувач вводить ціле число, програма виводить його останню цифру.
a = int(input("Введіть число"))
res = a%10
print(res)

#Користувач вводить довжину і ширину. Програма виводить периметр.
width = int(input("Введіть ширину"))
length = int(input("Введіть довжину"))
perimetr = 2*width+2*length
print("Периметр дорівнює=",perimetr)

#Написати програму, яка просить користувача ввести 4-х значне число з клавіатури, після чого друкує на екрані стовпчик цифр, з якого це число складається.
number = int(input("Введіть 4-х значне число"))
first_number = int(number//1000)
second_number = int((number%1000)/100)
third_number = int((number%100)//10)
fourth_number = int(number%10)
print(first_number)
print(second_number)
print(third_number)
print(fourth_number)