#Runtime and Big O notation

    #time != big O
    #if we are only measuring time on the clock, it can depend on how fast your hardware is
    #big O should be hardware independent
    
#Does the number of operations scale based on the input? How?

    #O(1) < O(logn) < O(n) < O(n^2)

    #O(1)/O(c) - constant time

        #best - most efficient

        #number of operations does not scale with increased input

        #it doesn't matter how much input, still has same number of operations

        #for example, accessing an item in an array. arr[1] will take the same amount of time if the length of the array is 2 or 2 million

        #same is true for a dictionary

        #it could be that it takes a million operations. If it is a million operations no matter if the input size is 2 or 5 of 10,000, still constant time, because they aren't dependant on each other.

        #graphed, constant time is a horizontal line. Y-offset might change, but will always be a horizontal line.
    
    #O(n) - linear time
    
        #number of operations begins to depend on input size

        def search(arr, target):
            for x in arr:
                if x == target:
                    return True
                else:
                    return False

        #if the above function took two elements, [1, 2] and we were looking for a target of 2.
            #think about the maximum number of times it could take to complete
            # at most, this would take 2 operations (but imagine an array of 1 million)

        #number of operations is directly proportional to the input size

        #Common to think a for loop is automatically O(n), but this is not always the case.

            def print_first_ten_arr_el(arr):
                for i in range(10):
                    print(arr[i])

            #in this case, we will only be looping over 10 elements regardless of input size, and this would be constant time or O(1)/O(c)

            def foo(arr):
                #step increments by 2
                for i in range(len(arr), step=2):
                    print(arr[i])

            #runtime ^ of foo would be O(n/2) or O(1/2 * n). HOWEVER, we disregard the constant, and boils down to O(n)

            #slope of the line may change, how fast increases, but it will always be a straight, diagonal line from the origin

#if you have two loops one after the other, add the runtimes together. For example a loop going through every other element, and next loop goes through the ones skipped, still leading to every element being iterated over, O(1/2n + 1/2n) = O(n)

#if you have nested loops, multiply the runtime

    for x in arr1:
        for y in arr2:
            print (x*y)


#Stacks
    #LIFO - last in, first out.
    #imagine stacking dishes in the cupboard. Whatever is added to the top (last in) will be the first one to be used (first out)
    #order is strict
    #think of these as vertical

#Queues
    #FIFO - first in, first out
    #think of these as horizontal, modeled after real-life queueing
    #last person in line will be coming out last. Order as they were put in is preserved

#stacks and queues are conceptual, not actual physical things that exist in python or any programming language

#Implementation
    #List in python has push and pop. 


#Linked Lists
    #arrays and linked lists store things in order 
        #arrays allow you to fetch particular elements by index
    #if arrays are a continuous block, a linked list is a chain


class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node
  def get_value(self):
    return self.value
  def get_next(self):
    return self.next_node
  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next


ll = Node(1)
ll.next_node = Node(2)
ll.next_node.next_node = Node(3)
ll.next_node.next_node.next_node = Node(4)

ll = Node(1)
ll_2 = Node(2)
ll_2.set_next(ll_2)
#etc

#have to do it that way because each individual node doesn't have access to the others

#define a class that encompasses the whole list

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, value):
        #need to wrap value in Node regardless
        new_node = Node(value)
        #what if the list is empty?
            #if there is no head
        if not self.head:
            self.head = new_node

            #value is just a the value, isn't wrapped in a node, should be the head

        #what if the list isn't empty?
        else:
            #add new node to the tail
            #can get to last node by traversing it
            current = self.head
            #if it is not none, there is a node after that one. At the end of the list get_next should return None
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)

    def remove_from_head(self):
        #what if the list is empty?
        if not self.head:
            return None
        #what if it isn't empty?
        else:
            #return value at current head
            value = self.head.get_value()
            #remove value at head
            #update self.head
            self.head = self.head.get_next()
            return value
            
        #the else just moves the pointer to the head element from the first element to the second element. It doesn't actually get rid of anything, but since linked lists only flow in a single direction, and head was the only way to access to the first element, it is effectively non-existent
