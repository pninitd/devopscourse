
# 1: Write a program which prints 'Hello' on screen and then print your name on a separate line.
print("#Ex1: ")
print("Hello \nPninit")
print()

# 2. Write a program to print the sum of two numbers
print("#Ex2: ")
num1 = 3
num2 = 6
print(num1 + num2)
print()

# 3. Write a program which will print the Python version number installed on your machine.
print("#Ex3: ")
import sys
print(sys.version)
print()

# 4. Write a program which will reverse a word
print("#Ex4: ")
str = "something"
result = ""
for i in reversed(str):
    result += i
print(result)

print()

# 5. Write a program which will print the amount of letters in a given word
print("#Ex5: ")
str = "hello"
count = 0
for i in str:
    count += 1
print("number of letters in \"%s\" is: %d" % (str, count))

print()

# 6. Write a program which will print the current date and time
print("#Ex6: ")
from datetime import datetime

now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

print()
# 7. Write a program which:
print("#Ex7: ")
x = 1
y = 5
if x > y:
    print(x, "is the bigger number")
elif x < y:
    print(y, "is the bigger number")
else:
    print(x, y, " - numbers are equal")

print()

# 8. Write a program which will check whether or not the number 120 is bigger than 5 and smaller than 200, if so, print MATCH
print("#Ex8: ")
number = 120
if number > 5 and number < 200:
    print("MATCH")

