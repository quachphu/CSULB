from Interfaces import Queue


class SLLQueue(Queue):
    class Node:
        def __init__(self, x: object):
            self.next = None
            self.x = x

    def __init__(self):
        """
        constructor; initializes an empty SLLQueue
        """
        self.head = None
        self.tail = None
        self.n = 0

    def add(self, x: object):
        """
        adds an element to the tail of the queue
        :param x: object type; the new element
        """
        new_node = SLLQueue.Node(x)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.n += 1

    def remove(self) -> object:
        """
        removes and returns the head of the queue
        :return: object type; the element that was removed from the head of the queue
        :raises: IndexError if the queue is empty
        """
        if self.head is None:
          raise IndexError("Queue is empty")
        else:
          removed_item = self.head.x
          self.head = self.head.next
          if self.head is None:
              self.tail = None
          self.n -= 1
          return removed_item

    def reverse(self):
        """
        reverses the order of the queue
        """
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def size(self) -> int:
        """
        returns the number of elements in the queue
        :return: int type
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