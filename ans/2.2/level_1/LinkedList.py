from __future__ import print_function
from Node import Node

class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.setNext(self.tail)
        self.tail.setPrev(self.head)

    def insert(self, index, element):
        if index > self.size:
            return
        else:
            node = self.head
            for i in range(0, index):
                node = node.getNext()
            new_node = Node(element)

            new_node.setNext(node)
            new_node.setPrev(node.getPrev())

            new_node.getPrev().setNext(new_node)
            new_node.getNext().setPrev(new_node)

            self.size+=1

    def prepend(self, element):
        old_front = self.head.getNext()

        self.new_front = Node(element)
        self.new_front.setNext(old_front)
        self.new_front.setPrev(self.head)

        # relink previous first node and head
        old_front.setPrev(self.new_front)
        self.head.setNext(self.new_front)
        self.size+=1



    def append(self, element):
        old_back = self.tail.getPrev()
        # make new node and link it
        self.new_back = Node(element)
        self.new_back.setPrev(old_back)
        self.new_back.setNext(self.tail)
        # relink previous last node and tail
        old_back.setNext(self.new_back)
        self.tail.setPrev(self.new_back)
        self.size+=1

    def get(self, index):
        node = self.head
        for i in range(0, index):
            node = node.next
        return node

    def front(self):
        # can check if empty but returns None, same thing
        return self.head.getNext()

    def back(self):
        # can check if empty but returns None, same thing
        return self.tail.getPrev()

    def search(self, element):
        node = self.head
        for index in range(1, self.size):
            if node.getNext().getElement() == element:
                return index
            node = node.getNext()
        return None

    def remove(self, index):
        if index > self.size:
            return
        else:
            # traverse list
            rm_node = self.head
            for i in range(0, index):
                rm_node = rm_node.next

            # gather surrounding nodes
            prev = rm_node.getPrev()
            next = rm_node.getNext()

            # relink surrounding nodes to each other
            prev.setNext(next)
            next.setPrev(prev)

            # call destructor for unlinked node
            rm_node.__del__()
            self.size-=1


    def popFront(self):
        if self.empty():
            return None
        else:
            pop_node = self.head.getNext()
            self.head.setNext(pop_node.getNext())
            pop_node.getNext().setPrev(self.head)
            self.size-=1
            return pop_node.__del__()


    def popBack(self):
        if self.empty():
            return None
        else:
            pop_node = self.tail.getPrev()
            self.tail.setPrev(pop_node.getPrev())
            pop_node.getPrev().setNext(self.tail)
            self.size-=1
            return pop_node.__del__()

    def getSize(self):
        return self.size

    def empty(self):
        if self.size == 0:
            return True
        else:
            False

    def printList(self):
        node = self.head.getNext()
        for i in range(0, self.size):
            print(node.getElement(), end=' ')
            node = node.getNext()
        print()

    def __del__(self):
        return self
