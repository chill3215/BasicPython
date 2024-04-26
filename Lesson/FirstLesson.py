# # how to print out
# print("Welcome to the World of Donut")
#
# # how to use variable and print out
# age = 20
# print("Your age is: ", age)
# exam_score = 1.5
# print("Deine Note ist", exam_score)
# name = 'Julia'
# print("I have a name friend, she is ", name)
# is_German = True
# print("Hier ist meine Freundin, sie heißt ", name, "und sie ist {}  years old".format(age))
#
# # receive input from the user
# inputName = input("What is your name? ")
# print("Hello {}".format(inputName))
#
# # convert variable to another type
# birth_year = input("Enter your birth year ")
# print("Your age is: ", 2024 - int(birth_year))
# # different from java, which is initialized with the type
# # and if type cast, (int) birth_year
# # bool(), str(), float()
# first_num = input("Enter the first number ")
# # first_num = int(3), int(input("first_num")
# second_num = input("Enter the second number ")
# # as input, the type of variable is automatically string
# # use '+' to concat the string
# print("sum" + str(float(first_num) + float(second_num)))
#
# # string
# course = 'Python for Beginners'
# # string wird als ein Objekt betrachtet, und die Methode werden durch das Obj aufgerufen
# print(course.find('y'))
# print(course.upper())
# # python is case sensitive
# print(course.find("For"))
# # Die oben gennaten Methoden werden String nicht ändern, weil String immutable ist
# print('Python' in course)
# index = course.find('n')
# print(index)

# arithmetische Operation
print(10/3)
# in Java gibt die Ganze zurück
# in java (float) 10/3 für das ungerundete Ergebnis
print(10//3)
print(10%3)
# die Methode für den Rest ist ähnlich wie in Java
print(10 ** 3)
# in Java Math.pow(10,3)
# für Dekrement und Inkrement und die anderen Operationen ist in Java gleich x += 3

# Operationen für Vergleichung
x = 3 != 2
print(x)

# logical operation
price = 25
print(price > 10 and price < 30)
# and or notcd


