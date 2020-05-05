# pass by reference vs pass-by-value
# https://blog.penjee.com/wp-content/uploads/2015/02/pass-by-reference-vs-pass-by-value-animation.gif
# define a function that multiplies input by 2


#passes it's input by value
def mult_by_2(x):
    return x * 2

y=12
# print(id(y))
z = mult_by_2(y)
# print(id(y))
print(z)

#is a new 12 getting passed in to the function or is it the same 12 in the same place in memory?
    #pass-by-value means we copy the input first, and then pass it in to the function
    #an integer will not ever be passed by reference, so it will always copy first
    #the original integer is not affected
#pass-by-reference
def mult2_list(l):
    #mult every int in list by 2
    #mutate the contents of the list
    for i in range(len(l)):
        l[i] *= 2

l = [1,2,3]
# print(id(l))
mult2_list(l)
# print(id(l))
print(l)
#if we have a list [1,2,3], the list is NOT copied and passed into the function
#the memory address of the original list is passed in
#the contents of the list will be mutated
#typically, data structures passed to a function are passed in by reference
    #this is because they can take up a lot of memory
    #copying would be expensive


#strings are immutable, and thus must be passed in by value


#CLASSES

#They allow us to define how we want to bundle different pieces of data together
#They allow us to persist that data


#Start by cataloging what we already know
    #define what median means
        #the middle element of all the elements after being sorted
    #figure out how to calculate it

#constructor() in js === def __init__
#every method will have self as an argument
    #can give __init__ second argument to pass something into the function

class MedianFetcherOutline:
    def __init__(self):
        #define all the attributes on 'self', similar to 'this' in JS
        self.median = None
        #None is approx the same as null and undefined

    #inserts the value n into our class
    def insert(self, n):
        #where do we store n?
            #maybe we store it in self.median?
            #what happens when we insert more values?

    def get_median():
        pass



class MedianFetcher:
    def __init__(self):
        self.median = None
        self.numbers = []

    def insert(self, n):
        pass

    def get_median():
        pass