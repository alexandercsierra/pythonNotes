#Binary Search Trees

#recursive version of get max
def get_max(self):
    if not self.right:
        return self.value
    self.right.get_max()



#iterative version of get max

def iterative_get_max(self):
    current_max = self.value
    #traverse our structure and update current_max if we see a larger value
    current = self
    while current is not None:
        if current.value > current_max:
            current_max = current.value
        current = current.right
    return current_max


#recursion uses a stack. Not one we have access to, but it keeps an order of function calls to be executed later. Callstack is LIFO


#iterative for_each (depth-first)

def for_each(self, fn):
    stack = []

    stack.append(self)

    when len(stack)>0:
        current = stack.pop()
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
        fn(current.value)


from collections import deque

def breadth_first_for_each(self, fn):
    queue = deque()

    queue.append(self)

    while len(queue) > 0:
        current = queue.popleft()
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        fn(current.value)