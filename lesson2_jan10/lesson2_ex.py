# A
print("##### A #####")
x = 10
y = 23
if x > y:
    print("BIG")
else:
    print("small")

print("##### B #####")
for x in range(5):
    print(x)

print("##### C #####")
season = 3
if season == 1:
    print("summer")
elif season == 2:
    print("winter")
elif season == 3:
    print("fall")
elif season == 4:
    print("spring")

print("##### D #####")
# 1 - loop will run 10 times
# 2 - last run will print 10
count = 1
while count < 11:
    print(count)
    count += 1

print("##### E #####")
my_age = 30
first_letter = "d"
currency = 3.26
flew = True
apartment_num = 20

print(my_age)
print(first_letter)
print(currency)
print(flew)
print(apartment_num)
print(currency + my_age)

print("##### F #####")
phone_number = input("Enter your phone number: ")
print("phone number ", phone_number)

print("##### G #####")


def printHello():
    print("hello")


def calculate():
    print(5 + 3.2)


print("##### H #####")


def printName(name):
    print(name)


def printdiv(num):
    print(num / 2)


print("##### I #####")


def addNumbers(num1, num2):
    return num1 + num2


def addSpace(str1, str2):
    return str1 + " " + str2


print("##### J #####")
# use list as array
arr = [3, 15, 4]
for x in arr:
    print(x)

print("##### K #####")
list_num = [3, 15, 4]


def sum_list(some_list):
    sum = 0
    # for x in range(len(list_num)):
    for item in list_num:
        sum += item
    return sum


print(sum_list(list_num))

print("##### L #####")
my_dictionary = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
for item in my_dictionary.keys():
    print(item)

print("##### M #####")


def pyramid(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


n = 5
pyramid(n)

print("##### N #####")


def xshape(n):
    i = 0
    j = n - 1
    for row in range(n):
        for column in range(n):
            if (column == i or column == j):
                print("*", end="")
            else:
                print(" ", end="")
        print("\r")
        i += 1
        j -= 1


xshape(7)

print("##### O #####")


def get_user_number():
    return input("Enter a number: ")


def sum_digits(input_number):
    sum = 0
    num_str = str(input_number)
    for i in range(0, len(num_str)):
        sum += int(num_str[i])
    return sum


print(sum_digits(get_user_number()))

print("##### P #####")
# I didn't use 'join' since such solution will work only for strings
# s =  ''.join(x_tuple)

x_tuple = 1, 5, 7
s = ''
for x in x_tuple:
    s += str(x)
print(s)

print("##### Q #####")
list1 = [10, 20, 4, 45, 99]
print("Smallest number in the list is:", min(list1))
