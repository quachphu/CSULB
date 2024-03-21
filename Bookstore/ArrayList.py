import numpy as np
from Interfaces import List


class ArrayList(List):
    """
    ArrayList: Implementation of a List interface using Arrays.
    """

    def __init__(self):
        """
        constructor creates an empty ArrayList object
        """
        self.n = 0
        self.j = 0
        self.a = np.zeros(self.n, object)

    def resize(self):
        """
        resize: Create a new array and copy the old values.
        """
        new_array = np.zeros(2 * len(self.a), dtype=object)
        for i in range(self.n):
            new_array[i] = self.a[(self.j + i) % len(self.a)]
        self.a = new_array
        self.j = 0

    def get(self, i: int) -> object:
        """
        returns the element at position i
        :param i: int type; integer index of the element to access
        :raise IndexError: raises IndexError if i is negative or greater than or
        equal to the number of existing elements
        """
        if i < 0 or i >= self.n:
            raise IndexError("Index out of bounds")
        return self.a[(self.j + i) % len(self.a)]

    def set(self, i: int, x: object) -> object:
        """
        sets the value at index i to be x.
        :param i: int type; index of the element that will be replaced
        :param x: object type; i.e., any object
        :raise IndexError: raises IndexError if i is negative or greater than or
        equal to the number of existing elements
        :return object; returns the element that was replaced at index i
        """
        if i < 0 or i >= self.n:
          raise IndexError("Index out of bounds")
        old_value = self.a[(self.j + i) % len(self.a)]
        self.a[(self.j + i) % len(self.a)] = x
        return old_value

    def append(self, x: object):
        """
        adds a new element to the end of this list
        :param x: Object type; the new element to add
        :return: None
        """
        self.add(self.n, x)

    def add(self, i: int, x: object):
        """
        inserts a new element x at the given index i by shifting elements
        left or right depending on whether the new element is being inserted to
        the first-half or the second-half of the list.
        :param i: int type; index of the position where new element will be inserted
        :param x: object type; i.e., any object
        :raise IndexError: raises IndexError if i is negative or greater than or
        equal to the number of existing elements
        """
        if i < 0 or i > self.n:
          raise IndexError("Index out of bounds")
        if self.n + 1 > len(self.a):
          self.resize()
        if i < self.n / 2:
          for k in range(i):
              self.a[(self.j + k - 1) % len(self.a)] = self.a[(self.j + k) % len(self.a)]
          self.j = (self.j - 1) % len(self.a)
        else:
          for k in range(self.n, i, -1):
              self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k - 1) % len(self.a)]
        self.a[(self.j + i) % len(self.a)] = x
        self.n += 1

    def remove(self, i: int) -> object:
        """
        removes the element at index i by shifting elements
        left or right depending on whether the element to be removed is in
        the first-half or the second-half of the list.
        and returns it
        :param i: int type; the index of the element to be removed
        :return: Object type; the element at index i
        :raise IndexError: raises IndexError if i is negative or greater than or
        equal to the number of existing elements
        """
        if i < 0 or i >= self.n:
          raise IndexError("Index out of range")
        x = self.a[(i + self.j) % len(self.a)]
        if i < self.n - self.j:
          self.j = (self.j + 1)
   
    def size(self) -> int:
        """
        returns the size of this list
        :return: int type; the number of elements in this list
        """
        return self.n

    def index_of(self, x):
        """
        returns the list index of element x if exists in the list
        or None, otherwise.
        :param x: object type;
        :return: int type; the index of x in the list; None if x is not in the list
        """
        for i in range(self.a):
            if self.a[i] == x:
                return i
        return None

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i < self.n - 1:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[(self.iterator + self.j) % len(self.a)]
            self.iterator += 1
        else:
            raise StopIteration()
        return x
