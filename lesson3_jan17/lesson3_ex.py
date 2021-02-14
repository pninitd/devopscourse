import io

print("##### 1,2 #####")
try:
    a = 1 / 0
except ZeroDivisionError as e:
    print("Error: ", e)


print("##### 3 #####")
# code is legal, we can use finally without except
try:
    x = 1
finally:
    print("finally")


# print("##### 4 #####")
# "Except:" is general for catching all types of exceptions

# print("##### 5 #####")
# using "Except:" without specific type of exception handler will be hard to find the failure reason and handle it properly.

print("##### 6 #####")
# IOError - handel any input/output error
try:
    with open('some_file', 'r') as file:
        data = file.read()
except IOError as e:
    print("Could not read file:{0}".format(e.filename))

# ZeroDivisionError handle division by zero
try:
    x = 1/0
    print(x)
except ZeroDivisionError as e:
    print(e)

print("##### 7,8 #####")
try:
    with open('words.txt', 'a+') as file:
        file.write('pninit')
except IOError as e:
    print("Could not write to file:", e)
finally:
    file.close()

print("##### 9 #####")
try:
    with open('words.txt', 'r') as file:
        content = file.read()
        print(content)
except IOError as e:
    print("Could not read the file:", e)
finally:
    file.close()

print("##### 10 #####")

try:
    with open('hebrew.txt', 'a+', encoding='utf-8') as file:
        file.write('קורס דבאופס 2021')
        file.seek(0)
        content = file.read()
        print(content)
except io.UnsupportedOperation as e:
    print("unsupportedoperation error:", e)
except IOError as e:
    print("I/O error:", e)
finally:
    file.close()

print("##### 12 #####")