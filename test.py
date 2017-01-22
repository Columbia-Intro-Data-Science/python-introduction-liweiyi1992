from sys import argv 
filename, x, y = argv
x = float(x)
y = float(y)
z = x * y
print "%d multiplied by %d is equal to %d" % (x, y, z)