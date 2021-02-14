
# ExA:
print("#ExA:")
first = 7
second = 44.3
print("add result:", first + second)
print("mult result", first * second)
print("div result:", second / first)
print()


# ExB: a: 9, b: 8, c: 15
print("#ExB:")
a = 8
a = 17
a = 9
b = 6
c = a + b
b = c + a
b = 8
print("a: %d, b: %d, c: %d" % (a, b, c))
print()

# ExC:
# Answer is no difference, both type string
print("ExC:")
name = "john"
print("first name", name)
name = 'john'
print("second name", name)
print()


my_number = 5 + 5
print(type(my_number))
# print("result is: "+ my_number)
# issue is that "my_number" is from type int and "+" operator in print command is between same type
# so expecting to get string
# suggested solutions:
print("result is:", my_number)
print("result is: %d" % my_number)
print()

# ExD: result is 7
print("ExD:")
x = 5
y = 2.36
print(x + int(y))
print()

# ExE: assuming you meant for integers
print("ExE:")
x = int(input("enter first number: "))
y = int(input("enter second number: "))
if x > y:
    print("BIG")
else:
    print("small")
print()

# ExF:
print("ExF:")
season = int(input("enter number between 1-4: "))
if season == 1:
    print("summer")
elif season == 2:
    print("winter")
elif season == 3:
    print("fall")
elif season == 4:
    print("spring")
else:
    print("number is not between 1-4")
print()

#CHALLENGE:
a = 8
b = "123"
print(a+int(b))
print(a,b)
