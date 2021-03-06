def baz(a, b=[]):
    pass

def bazII(a, b=None):
    if b is None:
        b = []


'''
Lists, objects, dictionaries, sets should not be default values. Mutable types should not be used as default values in python, can cause problems

https://stackoverflow.com/questions/1132941/least-astonishment-and-the-mutable-default-argument
'''

def loop1(n):
    while n>0:
        print(n)
        n-=1
    
loop(5)

def loop2(n):
    if n < 1:
        return n
    print(n)
    loop2(n-1)

loop2(5)

# print numbers from n to 1 
#     print n 
#     then print numbers n-1 to 1


def makelist(n):
    l = []

    for i in range(n):
        l.append(i)
    return l

def makelist_recur(n):
    pass

# Structure and interpretation of computer programs
    #download for recursive practice



'''
How to Solve Graph Problems
---------------------------

1. translate the problem into graph terminology
2. build the graph
3. traverse/search

'''


def find_word_ladders(begin_word, end_word):
    visited = set()

    q = Queue()

    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()
        cur_word = path[-1] #get last node in path

        if cur_word not in visited:
            visited.add(cur_word)

            if cur_word == end_word:
                return path

            for neighbor in get_neighbors(cur_word):
                #if you pass in a list to list() will make a copy
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)

    #could not find a path to end_word
    return None


'''
Works without a graph class, just using a get_neighbors function

adj_list or matrix is really just answering the question, what are all the neighbors?
'''