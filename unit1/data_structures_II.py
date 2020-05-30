#arrays are contiguous blocks of memory - literally right next to each other

#if you have an array that would take up 4 blocks of memory, but you don't have 4 contiguous blocks available... it can become fragmented
    #too many arrays of varying sizes can make memory difficult to use

#In a linked list, it doesn't have to live in contiguous memory blocks, so it is more efficient in that way. The prev and next pointers point to where those values live.

#Arrays and Queues
    #if you try and dequeue the first element, you can't just get rid of the first element, because that would leave a gap

    #removing from end is constant time O(c)/O(1)

    #removing from any spot is linear time O(n)


#Linked Lists and Queues
    #if there is only a reference to the head, it will be O(n) to add on to the end, since you have to traverse the whole list to get there.

        #adding a reference to the tail sets this back to O(c) or O(1), constant time

    #Advantage with deleting from a linked list is we don't have to shift anything as we would in an array. If you deleted something from the beginning of an array, all the indexes must shift to fill the space
    
    #Disadvantage is there is no indexing. Can't say give me the node at index 2. You have to traverse the list one by one until you find the node you're looking for.

    #from collections import deque even faster than custom linked list

    from collections import deque 
    class Queue:
        def __init__(self):
            self.size = 0
            self.storage = deque()
        def __len__(self):
            return len(self.storage)
        def enqueue(self, value):
            self.storage.append(value)
        def dequeue(self):
            if self.storage:
            return self.storage.popleft()
            else:
            return None 

