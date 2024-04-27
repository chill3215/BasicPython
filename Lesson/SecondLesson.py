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

names = ['John', 'Doe', 'Jane']
print(names[0])
print(names[-1])
names[2] = 'Julia'
print(names)
print(names[0:2]) #excluding the element of index 2
# -1 represents the last element of the list



