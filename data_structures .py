# list
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
# print(matrix)
# print(matrix[0])
# print(matrix[1])

# here list() is built-in function
# number = list(range(19))
# print(number)

# unpicking list
# we can pass unlamted list to our list
# numbers = [1, 3, 4]
# first, second, *others = numbers
# print(others)

# loop over list

# numbers = [1, 2, 3, 4, 5, 6]
# for number in numbers:
#     print(numbers)

# accesing the index of list

# letters = ["a", "b", "c", "d"]
# for letter in enumerate(letters):
#     print(letter)

# adding and removeing items in list
# +++  Adding
# letters = ["a", "b", "c", "d"]
# letters.append("-")
# letters.insert(1, "---")
# print(letters)


# +++ Removeing
# letters = ["a", "b", "c", "d"]
# remove the last item
# letters.pop()
# letters.remove("a")
# letters.clear()
# print(letters)


# finding items by it's index
# letters = ["a", "b", "c", "d", "c", "c"]
# print(letters.index("b"))
# print(letters.count("c"))


# sorting list
# numbers = [1, 3, 2, 5, 10, 6, 15, 22]
# ++ A-Z
# numbers.sort()
# sorted()
# ++ Z-A
# numbers.sort(reverse=True)
# print(numbers)


# lambda function

# x = lambda a: a + 10
# print(x(4))

# x = lambda a, b: a + b
# print(x(21, 12))

# items = [
#     ("product1", 10),
#     ("product2", 9),
#     ("product3", 12),
# ]

# items.sort(key=lambda item: [1])
# print(items)
