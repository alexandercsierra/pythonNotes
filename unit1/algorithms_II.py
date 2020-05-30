#counting sort
    #requires us to know the 'max' value we'll be sorting
    #the total range of data we'll be sorting sits between and 0 and maximum
def counting_sort(arr, maximum=-1):
    if len(arr) == 0: #O(1)
        return arr #O(1)
    
    #if maximum is not given, we'll take the max value from the input array
    if maximum == -1: #O(1)
        maximum = max(arr) #O(n)

    #make a bunch of buckets (add one to include max value)
    #underscore is common when not actually using the iterator
    buckets = [0 for _ in range(maximum+1)] #O(max)

    for x in arr: #O(n)
        if x < 0:
            return "Error, negative numbers not allowed"
        buckets[x] += 1 #O(1)

    #loop through our buckets, starting at the smallest index
    j=0
    #this whole loop is reversing the tallying we did in the previous loop
    for i in range(len(buckets)): #O(n) or #O(max)
        while buckets[i] > 0:
            arr[j] = i
            j+=1
            buckets[i] -=1

    return arr

    #overall time complexity is linear. O(n) or O(max)


#recursive sorting

#QuickSort

    #divide and conquer
    #1. find a pivot
        #first, last, or middle
        #we will partition data around this pivot
    #2. Partition all the data around the pivot
        #move lower values to the left and higher values to the right
    #Repeat steps 1 and two for each subarray until they have a length of 1
    #runtime is O(nlogn)
        #first n must be there. It isn't possible to sort without touching every element
        #logn => moving stuff around after looking at each 
        #best possible runtime for general-purpose sorting algorithms

    #recursion
        #1. What's our base/terminating case?
        #2. If we aren't in the base case, how are we moving towards it?


def partition(data):
    #pick the first element in data as our pivot
    pivot = data[0]
    left = []
    right = []

    for x in data[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    return left, pivot, right


def quicksort(data):
    #base case
    if len(data) == 0:
        return data
    #this function handles picking the pivot and partitioning the data around the pivot
    left, pivot, right = partition(data)

    return quicksort(left) + [pivot] + quicksort(right)


#ip stands for in place
def part_ip(data, start, end):
    pivot = data[start]
    i = start + 1
    j = start + 1

    #partitioning step to move elements around the pivot
    while j <= end:
        if data[j] <= pivot:
            data[j], data[i] = data[i], data[j]
            i+=1
        j+=1
    
    #end up with left and right arrays, but first element still at the start. This will swap the value so it ends up in the correct position (middle)
    data[start], data[i-1] = data[i-1], data[start]
    #return the index of the pivot
    return i-1

def ip_quicksort(data, start=0, end=None):
    if end is None:
        end = len(data) -1

    #base case (indices meet)   
    if start == end:
        return data

    #returns index of the pivot
    index = part_ip(data, start, end)

    #left
    ip_quicksort(data, start, index-1)

    #right
    ip_quicksort(data, index+1, end)


