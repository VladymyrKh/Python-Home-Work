a = int(input("Введіть число "))
total = a
day = 24*60*60
hour = 60*60
minute = 60
days, remainder = divmod(total, day)
hours, remainder = divmod(remainder, hour)
minutes, remainder = divmod(remainder, minute)
seconds = remainder
if 11 <= days % 100 <= 14:
    days_word = "днів"
elif days % 10 == 1:
    days_word = "день"
elif 2 <= days % 10 <= 4:
    days_word = "дні"
else:
    days_word = "днів"
time = f"{days_word} {hours:02d}:{minutes:02d}:{seconds:02d}"
final_result = f"{days} {time}"
print(final_result)
