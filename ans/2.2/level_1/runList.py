import sys
from LinkedList import LinkedList
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

link = LinkedList()

for line in data:
    for elem in line:
        link.append(elem)

link.printList()
# print(link.getSize())
#
# print(link.search("forty"))
#
# link.insert(7, "fifty")
#
# link.printList()
# print(link.getSize())
# print(link.search("forty"))
# print(link.search("fifty"))
#
# link.popBack();
# link.printList();

print link.empty()
