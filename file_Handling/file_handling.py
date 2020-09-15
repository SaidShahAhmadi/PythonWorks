# reading Files
# x = open("testingFile.py", "r")
# print(x.read())

# Read the Lines
# just read the first line

# a = open("testingFile.py", "r")
# # print(a.readline())
# print(a.readlines())
# a.close()

f = open("testingFile.py", "a")
f.write("Now the file has more content!")
f.close()

# open and read the file after the appending:
f = open("testingFile.py", "r")
print(f.read())


# f = open("testingFile.py", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

# # open and read the file after the appending:
# f = open("testingFile.py", "r")
# print(f.read())
