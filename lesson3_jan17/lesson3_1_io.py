# r - read only
#text files should have encoding='utf-8'
my_file = open("file.txt", 'r', encoding='utf-8')
# content = my_file.read()
# print(content)

print("******************")
my_file = open("file.txt", 'a+')
# r+ - no guaranteed for position to write
# w - run over the existing text
# a - append to the end

my_file.write("\nsss")
# will bring cursor to the start, unless we will get empty print after write that cause cursor to be at the end
my_file.seek(0)
# another option is to close()
content = my_file.read()
print(content)
my_file.close()

print("******************")



