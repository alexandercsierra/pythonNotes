#Binary Search Trees
    #Begins with root node
    #left nodes are less in value than the root node
    #right nodes are greater than (or greater than or equal to depending on desired tree) the root value

    #They are more efficient because if we know the target value is for ex, greater than the root, and we have a balanced tree, we have automatically eliminated half of the tree and don't have to search through it.

    #Runtime for bst is O(log n) 
        #technically O(log2n) <= sub 2, hard to represent on a keyboard
        #theoretically halving the search space on every single iteration
    #as opposed to an array which would be O(n)


    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            if not self.right:
                return False
            return self.right.contains(target)


    #with recursion, you always need to define a stopping point, or else it will go on forever
    #function calls along the way haven't terminated until a concrete return has happened
        #root node target greater? self.right.contains
            #next node target greater? self.right.contains
                #etc, etc
                    #find target, return True
                #return True
            #return True
        #return True to original function call


    #'base cases' - when we can return a concrete value 
    #recursion's use of memory is not better than a loop
        #emphasis is more on readability?