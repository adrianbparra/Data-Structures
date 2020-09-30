"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        
        # if value < root got left
        if value < self.value:
            # if left value is none assign it
            if self.left is None:
                self.left = BSTNode(value)
            else:
            # if value exist in right then call the same function for the left node
                self.left.insert(value)

        #  if value is >= go right
        else:
            # if value is none assign it
            if self.right is None:
                self.right = BSTNode(value)
            # if value exist in right then call the same function for the right node
            else:
                self.right.insert(value)
            


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if target is self.value
        # if yes return true
        if self.value is target:
            return True
        # else no,
        else:
            # go right if target >= self.value
            if target >= self.value:
                # call the def contains on self.right if it exist
                if self.right:
                    return self.right.contains(target)
                # else return false
                else:
                    return False
            # go left if target < self.value 
            elif target < self.value:
                # call the def contains on self.left if it exist
                if self.left:
                    return self.left.contains(target)
                # else return false
                else:
                    return False

        
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        # loop until outmost right node.right is none 
        if self.right is None:
            # return node.value
            return self.value
        else:
            return self.right.get_max()
        

    # Delete the value
    # THIS IS NOT REQUIRED
    def delete(self,value):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the function recursively until left and right is none
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        

    # Part 2 -----------------------

    # Breath First Traversal BFT
        # finding the shortest path on a map from point to point

    # Depth first Traversal DFT
        #  finding the exit out of a maze

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # start going all the left first

        # check if left
            # recurse
        # print
        # check if right
            # recurse
        
        if self.left:
            self.left.in_order_print()
            
        print(self.value)
        
        if self.right:
            self.right.in_order_print()
        
        

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # FIFO
        # create a queue
        queue = list()
        # self is added to queue
        queue.append(self)

        while queue:
        # if left
            if queue[0].left:      
             # add to queue / print
                queue.append(queue[0].left)
        
        # if right 
            if queue[0].right:
            # add to queue / print
                queue.append(queue[0].right)
            
        # remove and print the first item in the list
            print(queue.pop(0).value)

    # ################# RECURSIVE ###########################

        #Does NOT work
         
        # if self.left:
        #     self.left.bft_print()

        # if self.right:
        #     self.right.bft_print()



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # LIFO
        # # create a stack to keep track of nodes
        stack = list()
        # add self to stack
        stack.append(self)
        # while something still in stack
        while len(stack) > 0:
            # remove and print the first value
            node = stack.pop()
            print(node.value)

            # check if value exisits
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

# ####################### RECURSIVE ########################
        # recursive was was that as a node is visited it print
        # the print is called first as soon as the function is called on the node

        # print(self.value)
        # if self.left:
        #     self.left.dft_print()
        # if self.right:
        #     self.right.dft_print()


    # Stretch Goals -------------------------------------------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        # same order as dft_print 
        # prints as each node starting from left or right but 
        # goes to the depth of the direction it started
        print(self.value)

        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        # print tree in reversal starting from the last leaf and going up
        # go up in levels while printing
        # calling the function first they all stack from left to right
        # as the function return it prints the value

        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()

        print(self.value)
        

    def in_order_dft(self):
        # if there is a node less than visit
        if self.left:
            self.left.in_order_print()

        # if no left print or function has returned from 
        print(self.value)
        
        # if 
        if self.right:
            self.right.in_order_print()

        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

print("in order")
bst.in_order_print()
print("BFT")
bst.bft_print()
print("DFT")
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
