#today get working solution
#tomorrow, optimize them

#First-pass Solutions - UPER

    #Overwhelmed? Start asking questions to help UNDERSTAND the problem
        #jot them down
        #write down visualizations of the solution
        #can we solve an easier version of the problem first?
        
        #FBR : Fast, Bad, Wrong (rong)
        #FBI : Fast, Bad, Inefficient?
            #start somewhere, doesn't have to be efficient, good, or right
            #it is easier to start somewhere and improve than to wait to start until it's perfect

            # Code it
            # Make it work
            # Make it performant
            # Review and optimize as needed

    # "If there is a problem you can't solve, then there is an easier problem you can solve. Find it."

#Find middle node of linked list
#https://gist.github.com/seanchen1991/3887a0315ca24fe4459bd704fcc60978

    #could get to last node with counter - 5
        #divide by two - 2
        #find node at "index" 2

    #have two pointers, one moving twice as fast as the other
        #when one is at the end
        #the other will be halfway

        #with an even number you can overshoot the end or stop before, either way will return one of the middle two nodes which is acceptable for this problem

#Find target in 2D matrix

# How do we traverse a matrix?
# Are nested loops acceptable?
# Would be backtracking/recursion be useful for this? 
# Can be target be negative?
# How do we take advantage of the fact the matrix is sorted?
# Can subarrays contain arrays themselves? No
# Can binary search help us? 

# Can we solve an easier version of the problem first?
# Change the problem to just be searching in a matrix? 

matrix = [[]]

# row indices
for i in range(len(matrix)):
    # column indices 
    for j in range(len(matrix[0])):
        if matrix[i][j] == target:
            return [i, j]


# iterate along the rows
for row in matrix:
    # iterate along the columns 
    for elem in row:
        if elem == target:

def merge(A, B):
    # init the combined list that will hold the sorted elements from both A and B
    # combined = [0] * (len(A) + len(B))
    # combined = [0 for _ in range(len(A) + len(B))]
    combined = []

    # init the two pointers that start at each list 
    a = 0
    b = 0

    while a < len(A) and b < len(B):
        # compare the elements that a and b point at 
        if A[a] < B[b]:
            combined.append(A[a])
            a += 1
        else:
            combined.append(B[b])
            b += 1

    # at this point, we've finished traversing one of the lists completely
    # we need to add all of the elements from the other list to the combined list 
    while a < len(A):
        combined.append(A[a])
        a += 1 
    while b < len(B):
        combined.append(B[b])
        b += 1

    return combined

def merge_sort(arr):
    # break the array down recursively
    # base case: when the lists get down to lengths of 1 
    if len(arr) > 1:
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)
    
    return arr



def merge_in_place(arr, start, mid, end):
	# start2 is the first element in the right
	# half of the list
    start2 = mid + 1

    # If the two halves we're merging are already
	# sorted, no need to do anything
    if arr[mid] <= arr[start2]:
        return

    # Two pointers to maintain start
    # of both arrays to merge
    while start <= mid and start2 <= end:

        # If element 1 is in right place
        if arr[start] <= arr[start2]:
            start += 1

        else:
            value = arr[start2]
            index = start2

            # Shift all the elements between element 1
            # element 2, right by 1.
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1
			
	# we don't return anything in in-place functions
	# since we're directly mutating the input array

def merge_sort_in_place(arr, l, r):
    if l < r:
        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2

        # Sort first and second halves
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)

        merge_in_place(arr, l, m, r)
     