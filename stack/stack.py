import sys  
sys.path.append("C:\\Users\PC1\Documents\Lambda_School\Data_Structures\Data-Structures\singly_linked_list")
from singly_linked_list import LinkedList,Node

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = list()
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        # add size up
        self.size +=1
        # add value to end
        # self.storage.append(value)
        self.storage.add_to_tail(value)

    def pop(self):
        # check if size == 0
        if self.size == 0:
            return None

        else:
            # subtract size
            self.size -= 1
            # return last value
            # return self.storage.pop()
            return self.storage.remove_tail()
