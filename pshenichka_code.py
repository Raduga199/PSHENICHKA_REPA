def pshenichka():
    print("This is a phenichka file")


pshenichka()

print("Hello, my_way!")
print("Today is the best day!")
print("Add some changes")


def func_prank(func):
    return func


def inner_func(name):
    print(f"{name}, let's start a game:D")


func_in_func = func_prank(inner_func)
func_in_func('Jane')
