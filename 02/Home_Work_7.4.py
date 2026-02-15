def common_elements():
    a = {x for x in range(100) if x % 3 == 0}
    b = {x for x in range(100) if x % 5 == 0}
    return a & b


print(common_elements())
