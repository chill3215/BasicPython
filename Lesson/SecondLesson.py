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

# tuple is like list but immutable
list = (1, 2, 3, 4, 5)
print(list.index(3, 0, len(list)))
print(list.__add__((6, 7, 8)))
print(list.__getitem__(0))



