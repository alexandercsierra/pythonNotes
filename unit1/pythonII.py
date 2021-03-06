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

# class MedianFetcherOutline:
#     def __init__(self):
#         #define all the attributes on 'self', similar to 'this' in JS
#         self.median = None
#         #None is approx the same as null and undefined
#         #Didn't end up using :shrug:

#     #inserts the value n into our class
#     def insert(self, n):
#         #where do we store n?
#             #maybe we store it in self.median?
#             #what happens when we insert more values?

#     def get_median():
#         pass



class MedianFetcher:
    def __init__(self):
        self.median = None
        self.numbers = []

    def insert(self, n):
        self.numbers.append(n) #can't chain methods, append doesn't return anything
        self.numbers.sort() #don't need to store it, will change original list. This could also be put at the beginning of get_median (maybe more efficient?)

    def get_median(self):
        if len(self.numbers) == 0:
            return None
        #is length of list odd or even?
        mid = len(self.numbers) // 2
        if len(self.numbers) % 2 == 1:
            #if odd, return middle number
            return self.numbers[mid]
        else:
            #if even, get the average of the two middle numbers
            #grab the element right before the mid element
            other = self.numbers[mid-1]
            return (other + self.numbers[mid])/2

#floor to get to closest whole number when dividing:
    # 5 // 2  would be equal to 2
    # you might think to add 1 to get middle number, but considering a zero index, you don't have to add 1

medianFetcher = MedianFetcher()
medianFetcher.insert(5)
medianFetcher.insert(10)
print(medianFetcher.get_median()) # should return 7.5