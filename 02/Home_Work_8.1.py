def add_one(some_list):
    number = int("".join(str(i) for i in some_list))
    number += 1
    return [int(i) for i in str(number)]


if (
    add_one([1, 2, 3, 4]) == [1, 2, 3, 5] and
    add_one([9, 9, 9]) == [1, 0, 0, 0] and
    add_one([0]) == [1] and
    add_one([9]) == [1, 0]
):
    print("ok")
else:
    print("you have mistakes")
