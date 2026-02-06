# Перетворити рядок на хештег
import string
user_words = input('Введіть текст для хештегу  ')
user_text = user_words.title()
for_removing = string.punctuation + ' '
table = str.maketrans('', '', for_removing)
hashtag = user_text.translate(table)
final_hashtag = '#' + hashtag
if len(final_hashtag) > 140:
    final_hashtag = final_hashtag[:140]
print(final_hashtag)
