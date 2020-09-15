# ternary operater
# age = 18
# if age >= 18:
#     print("Eligible")
# else:
#     print("Not Eligible")

# changing into ternary operater. Good way and clean way
# age = 18
# message = "Eligible" if age >= 18 else "No Eligible"
# print(message)

# -------------++++++++++++++++++++++++++--------------#
# loops
# for number in range(1, 11):
#     print("Number", number)


# forloop else
# succesfull = False
# for number in range(3):
#     print("Attempt")
#     if succesfull:
#         print("Succesfull")
#         break
# else:
#     print("Attempted 3 times succesful")

# While loop
# number = 12
# while number >= 0:
#     print("while loop")


# -------------++++++++++++++++++++++++++--------------#
# Data structures
# ++ lambda function

# def x(a): return a + 12
# print(x(12))

# Program to show the use of lambda functions
# def double(x): return x * 2
# print(double(5))

# items = [
#     ("product1", 10),
#     ("product2", 12),
#     ("product3", 9)
# ]

# items.sort(key=lambda item: item[1])
# print(items)

# map() function of lambda
# +++ example if we want find prices in the list
# prices = [1, 3, 4, 6, 8, 5]
# prices = list(map(lambda x: x*2, prices))
# print(prices)

# filter()
# exmple if we want find that prices is >= to 20 find it
# items = [
#     ("product1", 10),
#     ("product2", 30),
#     ("product3", 40)
# ]

# firltered = list(filter(lambda item: item[1] >= 20, items))
# print(firltered)

# Zip()  to jonined two or more list togeter
# list1 = [1, 2, 3, 4]
# list2 = [10, 23, 44]
# print(list(zip(list1, list2)))

# ++ or we can add string also

# list1 = [1, 2, 3, 4]
# list2 = [10, 23, 44]
# print(list(zip("abc", list1, list2)))

# -------------++++++++++++++++++++++++++--------------#

# Exception in python to handle errors

# try:
#     age = int(input("Your Age: "))
# except ValueError:
#     print("you don't enter a valid age.")
# else:
#     print("No exception")

# print("exception")


# with identifier
# show more information about error

# try:
#     age = int(input("Your Age: "))
# except ValueError as ex:
#     print("you don't enter a valid age.")
#     print(ex)
# else:
#     print("NO Excptions were throw")


# handle multiple exceptions
# TypeError and ZeroDivisionError
# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError) as ex:
#     print("Error:you don't enter a valid age. ")
# else:
#     print("NO Excptions were throw")


# raise in excptions
# +++ in this code if the age is negative so
# +++ the raise message will be show

# def calu_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be 0 or less then.:)")
#     return 10 / age


# try:
#     calu_xfactor(-2)
# except ValueError as error:
#     print(error)
