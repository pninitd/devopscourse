age = int(input("enter your age "))
if age>18:
    print("Adult")

password = "12345"
userpass = input("enter a password ")
if password == userpass:
    print("logged in")
else:
    print("Access denied")

age = int(input("enter your age "))
height = float(input("enter your height "))
if age > 12 and height > 160:
    print("OK")
else:
    print("Forbidden")
