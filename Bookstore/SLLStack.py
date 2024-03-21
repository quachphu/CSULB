from Interfaces import Stack
import numpy as np


class SLLStack(Stack):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.x = x

    def __init__(self):
        """
        constructor; initializes an empty stack
        """
        self.head = None
        self.n = 0

    def push(self, x: object):
        """
        adds a new element to the head of the stack
        :param x: object type; the new element
        """
        new_node = SLLStack.Node(x)
        new_node.next = self.head
        self.head = new_node
        self.n += 1

    def pop(self) -> object:
        """
        removes and returns the element at the head of the stack
        :return: object type; the element that was removed from the stack
        :raises: IndexError if the stack is empty
        """
        if self.head is None:
          raise IndexError("Stack is empty")
        else:
          removed_item = self.head.x
          self.head = self.head.next
          self.n -= 1
          return removed_item

    def size(self) -> int:
        """
        returns the number of elements in the stack
        :return: int type;
        """
        return self.n

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = self.head
        return self

    def __next__(self):
        if self.iterator != None:
            x = self.iterator.x
            self.iterator = self.iterator.next
        else:
            raise StopIteration()
        return x




