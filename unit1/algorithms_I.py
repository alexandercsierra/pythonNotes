#Determining Time Complexity
    #compute big O of each line in isolation
    #if something is in a loop, multiply big O by the number of iterations in the loop.
    #if two things happen sequentially, add the big Os
    #Drop leading multiplicative constants from each big O (2n => n, 1/2n => n  n/2 => n)
    #From all the big-Os that are added, drop all but the biggest dominating one.

#Space or memory complexity measures how much additional memory algorthm alloactes in order to run

    #one big giveaway that an algorithm is utilizing additional memory is it if intializes a data structure

#O(n) time, O(1) space
def o_1_space(n):
    total = 0 #O(1)

    for i in range(n):
        total +=i #space wise, contributes nothing O(1)

    return total

#most numbers take amount of space in memory (0 or 1000)

#zero is taking constant space

#O(n) time, O(n) space
def o_n_space(n):
    sums = []

    for i in range(n):
        sums.append(i+1) #for each n, we are appending a number, so we are appending O(n) things
    
    return sums

#adding values to some data structure, one for each input

def o_n2_space(n):
    times_table = []

    for i in range(n): #O(n)
        row=[]

        for j in range(n):
            row.append(j*i) #adding elements to the row list for each n. O(n)
        
        times_table.append(row) #we have n lists that each hold n elements O(n)

    return times_table #O(n^2)

    #each row had 5 numbers, there will be 5 rows added to times_table. 5^2 = 25 total output numbers. O(n^2)


#O(1)
def foo(arr):
    for x in arr:
        print(x+x)

#space complexity cares about how much ADDITIONAL space is being used
    #if we are given an array upfront, it doesn't add to space complexity. It doesn't add more.


def bar(arr):
    output = []

    for n in arr:
        output.append(n*n) #O(n)

    return output

#here we are creating a new array besides the one given to us


#assume that arr contains numbers 1-10
def baz(arr):
    evens = []

    #adding half of the values from the input array
    for n in arr:
        if n%2 == 0:
            evens.append(n) #O(n/2) => O(n) space

    return evens




#Most of the time, looking to optimize time complexity, rather than space. Often optimizing time uses data structures that cost more space.

#pass by reference - passing an array into a function, the function is receiving a pointer to the inpu

#pass by value - the function is receiving a copy of the input

#neither counts against a function just because it is passed in


def o_2_space_v2(n):
    times_table=[]

    for i in range = []
        times_table.append(i)

        for j in range(n):
            times_table.append(j)

    return times_table

#O(n^2) space



#SEARCHING

#databases are indexed - means they aren't looking through every item. There's an order to it


# [1,2,3,4,5,6,7,8,9,10]
# can find something in this array more easily because it is sorted

#target = 2
arr = [1,2,3,4,5,6,7,8,9,10]
#first find the midpoint
midpoint = len(arr)//2 #5
arr[5] = 6 #midpoint is 6
#discard arr[5] and anything greater
#find new midpoint of 3
#continue until find 2

#took 3 checks to find. 10 inputs, log2 * 10 = 3 . so O(logn)



#assume arr is sorted
#returns index of target if it exists in the arr
#otherwise return -1
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    #may need to go right where index is not starting at zero

    while left <= right:
        mid = (left + right) // 2

        #check to see if midpoint is target
        if arr[mid] == target:
            return mid

        #check to see if the element should be on the left or right side of our midpoint
        if arr[mid] < target
            #toss out the left side of arr
            left = mid + 1

        #mid is greater than
        else:
            #toss out the right side of arr
            right = mid - 1

    #didn't find target
    return -1


#Insertion Sort

# 6 3 5 1 => 3 6 5 1 => 3 5 6 1 => 1 3 5 6

class Book: 
    def __init__(self, title, author, genre):
        self.title = title
        self.auther = author
        self.genre = genre

def insersion_sort_books(arr_of_books):
    #sort by title

    #starting at 1 because we don't need to compare the index of the first thing to itself
    for i in range(1, len(arr_of_books)):
        curr_book = arr_of_books[i]
        j=i
        #put curr_book in the appropriate spot in our sorted half

        #loop through sorted half and find appropriate spot
        #j-1 is the previous element
        while j > 0 and curr_book.title < arr_of_books[j-1].title:
            #slide curr_book over. 
            #swap them
            # arr[j], arr[j-1] = arr[j-1], arr[j]
            arr_of_books[j] = arr_of_books[j-1]
            j -= 1

        arr_of_books[j] = curr_book

    return arr_of_books