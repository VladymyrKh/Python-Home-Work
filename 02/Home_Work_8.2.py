def is_palindrome(text):
    final_text = ""
    for char in text:
        if char.isalnum():
            final_text += char.lower()
    return final_text == final_text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ok")

