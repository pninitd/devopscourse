# Lists are mutable- can change their content without changing the types
my_list = [5, "a", True]

# modify specific index
my_list[0] = 4
print(my_list[0])

# adding an element
my_list.append(111)

# removing an element
my_list.pop(0)
print(my_list)

# adding an element to a specific index
my_list.insert(1, 7)
print(my_list)

print("*** exercises ***")
# 1. create a list with 3 elements
list = ["a", 4, 9]
# 2. print second element
print(list[1])
# 3. modify second element value
list[1] = 12
print(list[1])
# 4. insert a new element to the second index
list.insert(1, "second")
print(list)

print("size of list: ", len(list))
for temp in list:
    print(temp)
print("***** loop2 ****")
for i in range(len(list)):
    print(list[i])

# immutable - we cannot add/remove/modify the values
x_tuple = 1, 5, 7
print(x_tuple)
for x in x_tuple:
  print(x)
  
print()

print("***** Dictionary ******")
my_dictionary = {'A': 1, 'B': 2, 'C': 3, 'D': 4 }
my_dictionary['A'] = 5
print(my_dictionary.keys())
print(my_dictionary.values())

del(my_dictionary['A'])
print(my_dictionary)
