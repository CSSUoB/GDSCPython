import sys
fileName = sys.argv[1]
file = open(fileName, "w")
file.write("Hello world!")
file.close()
