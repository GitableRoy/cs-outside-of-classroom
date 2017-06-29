import sys
from Array import Array

data = []
try:
    with open(''+ sys.argv[1] +'', 'r') as inputfile:
        for line in  inputfile:
            data.append(line.strip().split(' '))
except Exception as e:
    raise
else:
    exit

array = Array(10)
array.printArray()

array.insert(5, "yeah")
array.printArray()

array.prepend("pre")
array.printArray()

array.append("app")
array.printArray()

print(array.get(5))
print(array.front())
print(array.back())

print(array.search("yeah"))

array.remove(5)
print(array.get(5))

print(array.popFront())
print(array.popBack())
array.printArray()

print array.getSize()
print array.__del__()
