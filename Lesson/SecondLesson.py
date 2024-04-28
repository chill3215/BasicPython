# # if statement
# temperature = 34
# if temperature > 30:
#     print("It's a hot day")
#     if temperature > 35:
#         print("Put on suncream before going out")
#
#     elif temperature > 33:
#         print("Stay hydrated")
#     else:
#         print("Just be normal")
# # use double quote so that the single quote can be seen as a part of the string
# # use indentation to express a block of code
# # indentation means lines start further away from the edge
# print("Done")
#
# weight =  float(input("Weight: "))
# unit = input("(K)g or (L)bs: ")
#
# if unit.lower() == "kg":
#     weight = weight * 2.2
#     unit = "lbs"
# elif unit.lower() == "lbs":
#     weight = weight * 0.45
#     unit = "kg"
# print("Weight in {} unit is ".format(unit), weight)

# loop
# i = 1
# while i <= 1_0:
#     print(i)
#     i += 1
# while i <= 10:
#     print(i * "*")
#     i += 1
#the string will be repeated i times

# i = 1
# # i runs from i to 9
# for i in range(10):
#     print("{}: ".format(i), i * "+")

# names = ['John', 'Doe', 'Jane']
# print(names[0])
# print(names[-1])
# names[2] = 'Julia'
# print(names)
# print(names[0:2]) #excluding the element of index 2
# -1 represents the last element of the list
#
# # list methods
# numbers = [1, 2, 3, 4, 5]
# numbers.append(6)
# numbers.insert(0,1)
# numbers.remove(3)
# print(numbers)
# print(1 in numbers)
# print(len(numbers))
# for i in numbers:
#     # just line for(int i: numbers) in java
#     print(i)
# # there isnt any print and println in python, print will automatically enter when executed

# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i += 1
#
# # use range function to generate a sequence of numbers
# range(5)
# # from 0 to 4
# for numbers in range(5, 10, 2):
#     print(numbers)

# # tuple is like list but immutable
# list = (1, 2, 3, 4, 5)
# print(list.index(3, 0, len(list)))
# print(list.__add__((6, 7, 8)))
# print(list.__getitem__(0))

# # this is also a tuple
# # tuple packing, the reverse is call sequence unpacking
# tuple3 = 1, 2, 3
# print(tuple3)
#
# tuple = ()
# # this tuple is empty
# print(len(tuple))
#
# # this tuple is not empty, parenthesis can be ommited
# tuple2 = 'a',
# print(len(tuple2))

# # how to add new value to dictionary
# dic1 = {"a": [1], "b": [2], "c": [3], "d": 4}
# print(dic1)
#
# # only added temporarily, locally, not in memory
# dic1["a"].__add__([3])
# print(dic1["a"])
# # add to the value to an already existed key
# dic1["a"].append(2)
# print(dic1["a"])
# for k, v in dic1.items():
#     print(f"key: {k}, value: {v}")
#     print("{}".format(k))
# del dic1["a"]

# # iterate and get index and corresponding values at the same time
# list4 = ['a', 'b', 'c']
# for index, value in enumerate(list4):
#     print(f"index: {index}, value: {value}")
#
# # iterate2 sequence at the same time
# attribute = ['name', 'size', 'price']
# value = ['suncream', '100ml', '$30']
# for attr, val in zip(attribute, value):
#     print(f"{attr}: {val}")
#     print("{0}: {1}".format(attr, val))
#
# for i in reversed(range(2, 10, 2)):
#     print(i)

# list = [1, 2, 3, 4, 5, 5, 2, 6, 7, 8, 9]
# for i in set(list):
#     print(i)

# change can be taken on the list level, not the tuple level
tuple = ([1, 2, 3], [4, 5, 1])
print(tuple)
tuple[0].append(1)
tuple[0][1] = 7
# tuple[0] = [1, 1, 1, 1, 1] false
print(tuple)

list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
list.append((7, 8, 9))
list[0] = (7, 8, 9)
# list[0][1] = 3
print(list)
