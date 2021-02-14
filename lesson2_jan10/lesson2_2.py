import datetime
import time


def calculate():
    x = 1
    y = 4
    print(x + y)

calculate()


def print_name():
    print("Hi Pninit")


def get_name_print(name):
    print("hello " + name)


def get_name():
    return "Pninit"


def add_num(n1, n2):
    return n1 + n2

# 1. function which prints your name
print_name()
# 2. function which gets a name and prints it
get_name_print("pninit")
# 3. function return your name
name = get_name()
print(name)
# 4. function which gets 2 nums and returns their addition value
add_result = add_num(4, 6)
print(add_result)

print("***** using yield bad practice ***")
def yield_test():
    yield 1
    time.sleep(2)
    yield 2


for value in yield_test():
    print(value)

print("***** datetime ***")
print(datetime.datetime.now())

