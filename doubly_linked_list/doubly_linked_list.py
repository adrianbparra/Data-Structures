"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    # adding to tail
    def insert_after(self,prev):
        prev.next = self
        self.prev = prev
        
    # adding to head
    def insert_before(self,next):
        next.prev = self
        self.next = next
        
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create node
        node = ListNode(value)
        # add to empty
        if self.head is None:
            # update head and tail
            self.head = node
            self.tail = node
            pass
        # add to not empty
        else:
            # update cur self.head to node.next
            node.next = self.head
            # update cur self.head.prev value to node
            self.head.prev = node
            #update head
            self.head = node
            pass
        # update lenght
        self.length += 1
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # check if node
        # cant we just use delete and have node as self.head
        value = self.head.value
        self.delete(self.head)
        #  
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # wrap value to list node
        # node = ListNode(value)
        # # check no values
        # if self.tail is None:
        #     self.tail = node
        #     self.head = node
        # # else
        # else:
        #     # update self.tail.next to node
        #     self.tail.next = node
        #     # update node.prev to self.tail
        #     node.prev = self.tail
        #     # update new self.tail to node
        #     self.tail = node
        #     pass
        # self.length += 1
        pass
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # saves value of tail
        value = self.tail.value
        # deletes tail with delete()
        self.delete(self.tail)
        # return value
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        
        if self.head is node:
            return 
        # delete 
        self.delete(node)

        self.add_to_head(node.value)
        
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # check if no values
        if self.tail is None:
            return
        # delete function
        self.delete(node)
        # add to tail on node
        self.add_to_tail(node.value)
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # what is node is not found or node has no prev or next values
        if self.head is None:
            return None

        elif self.head is self.tail:
            self.head = None
            self.tail = None

        elif node is self.head:
            self.head = node.next
            node.delete()
            
        elif node is self.tail:
            self.tail = node.prev
            node.delete()

        else:
        # many values
        # has to update position for prev and next only
            node.delete()
            pass    

        self.length -= 1
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):

        # check if there is node
        if self.head == None:
            return None
            
        value = 0
        cur_node = self.head
        # start with value as 0 and cur_node as head
        # loop over while cur_node is not none
        while cur_node is not None:
        # check if cur_node.value is > value else nothing
            if cur_node.value >= value:
                value = cur_node.value
            
            cur_node = cur_node.next
        # return value
        return value


list = DoublyLinkedList()

# print(list.get_max())
# list.add_to_tail(185)
# list.add_to_head(22)
# list.add_to_tail(25)

# print(list.get_max())