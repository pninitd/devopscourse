for x in range(50):
    print(x)

print("**************")
for x in range(3, 5):
    print(x)

print("**************")
for x in range(3, 8, 2):
    print(x)

print("****** while Loop with break********")
count = 0
while count < 50:
    if count == 3:
        break
    print(count)
    count += 1


print("****** while Loop with continue********")
count = 0
while count < 50:
    count += 1
    if count == 3:
        continue
    print(count)


print("******* functions *******")
def main():
    print("hello")
if __name__ == '__main__':
    main()

