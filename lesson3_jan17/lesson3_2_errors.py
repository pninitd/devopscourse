import io

try:
    f = open("file.txt", 'r')
    f.write('hello')
except io.UnsupportedOperation as e:
    print("unsupportedoperation error...", e)
except IOError as e:
    print("io error...", e)
except Exception as e:
    print("general error...", e)
finally:
    f.close()
    print("finally")
print(1)

#SystemExit

print("*********************")
# another syntax, no need to close file at the end
with open("file.txt", 'w') as file:
    file.write('hello word!')



