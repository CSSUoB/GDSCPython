import sys

fileName = sys.argv[1]
file = open(fileName, "r")
print(file.read())
file.close()
