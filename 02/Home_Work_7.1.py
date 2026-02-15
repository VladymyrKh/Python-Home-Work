def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"


a = say_hi("Alex", 32)
b = say_hi("Frank", 68)
if (a == "Hi. My name is Alex and I'm 32 years old"
        and b == "Hi. My name is Frank and I'm 68 years old"):
    print('ОК')
else:
    print('You have a mistake')
