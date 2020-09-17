
class Node:
    def __init__(self,value = None, next_node = None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def set_value(self,value):
        self.value = value

    def set_next_node(self,next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self,value):
        cur_node = Node(value)
        # check if no head
        if self.head == None:
            self.head = cur_node
            self.tail = cur_node
        else:
            cur_node.set_next_node(self.head)
            self.head = cur_node

    def get_head(self):
        return self.head


    def remove_head(self):
        if self.head == None:
        # check if no head
            return None
        elif self.head == self.tail:
        # only one node
            temp = self.head
            self.head = None
            self.tail = None
            return temp.get_value()
        else:
        # many node 
            temp = self.head
            self.head = temp.get_next_node()

            return temp.get_value() 

    def add_to_tail(self,value):
        cur_node = Node(value)
        if self.tail == None:
        # check if no nodes
            self.head = cur_node
            self.tail = cur_node
        else:
        # else update tail
            # add the value node to curr tail node
            self.tail.set_next_node(cur_node)
            # update tail to value node
            self.tail = cur_node

    def get_tail(self):
        return self.tail

    def remove_tail(self):
        # check if no nodes
        if self.tail == None:
            return None
        # if only one node
        elif self.head == self.tail:
            # save temp
            temp = self.tail
            # set tail and head to none
            self.tail = None
            self.head = None
            # return temp value
            return temp.get_value()
            pass
        # many node
        else:
            # loop over until node's get next node it tail node
            cur_node = self.head
            while cur_node.get_next_node() is not self.tail:

                cur_node = cur_node.get_next_node()
            # save temp tail
            temp = self.tail
            # remove node get next node
            cur_node.set_next_node(None)
            # save node as tail
            self.tail = cur_node

            return temp.get_value()
            
        pass

    def contains(self,value):
        # save head node
        cur_node = self.head
        # if no nodes
        if cur_node is None:
            return None
        # loop over until value found
        while cur_node is not None:
        # return true if found
            if cur_node.get_value() == value:
                return True

            cur_node = cur_node.get_next_node()
        # return false if no value found
        return False
        pass 

    def get_max(self):
        # save current head value
        max_value = 0
        cur_node = self.head
        # if cur node is none
        if cur_node is None:
            return None
        # loop over all node until cur node is none
        while cur_node is not None:
            # check if cur node value is bigger and save
            if cur_node.get_value() > max_value:
                max_value = cur_node.get_value()

            # update cur to next node
            cur_node = cur_node.get_next_node()

        # return value
        return max_value
        


list = LinkedList()
list.add_to_head(12)
list.add_to_tail(21)
list.add_to_tail(85)
list.add_to_tail(35)
list.add_to_tail(25)
list.add_to_tail(22)





# print(list.remove_head())
# print(list.get_max())
# print(list.remove_tail())

