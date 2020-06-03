"""
The general problem the hash table solves -

They search fast!

We can use it to store and retrieve the results of any slow operation with the key as the input and the value as the output


Think of a cache is an application of a hash table
"""

#0 and 1 return 1, otherwise retruns the sum of the two numbers before it
#time complexity is O(2^n) - every time we call this function it gets called 2 more times inside of itself, then 2 more times for each of those, etc
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

    #would take a long time
    for i in range(50):
        print(f'{i} {fib(i)}')
"""
We will be computing the same numbers over and over
fib(30) = fib(29) + fib(28)
fib(29) = fib(28) + fib(27)
fib(28) = fib(27) + fib(26)

"""
cache = {}
def fib(n):
    if n<=1:
        return n
    #if n is not a key in the cache
    if n not in cache:
        #add it
        cache[n] = fib(n-1) + fib(n-2)
    return cache[n]


#any immutable type as a key - tuple is also immutable
def expensive_function(x,y):
    key = (x,y)

    if key not in cache:
        cache[key] = whatever_expensive_thing_here()

    return cache[key]


#inverse square root
# inv_sqrt(x) = 1/sqrt(x)  <= this is an expensive computation

#here we are building it ahead of time before we invoke with any value, instead of above where we were computing as we went
import math

inv_sqrt = {}

def build_lookup_table():

    for i in range(1, 1000):
        inv_sqrt[i] = 1 / math.sqrt(i)
build_lookup_table()
print(inv_sqrt[3])
print(inv_sqrt[12])


#Let's sort a dictionary/hash table
    #should convert to a list so we can use the sort method
    #.items() returns an 'iterator' of tuples, with the (key, value)
    #convert to a list

my_dict = {'a':2, 'b':3}

list(my_dict.items())
sorted(list(a.items()))

#sorted sorts in place instead of returning a new list
#sorted() = immutable, .sort() = mutable

d = {
    'foo': 12,
    'bar': 17,
    'qux': 2
}

items = list(d.items())
#sort ascending by key
items.sort()

print(items)

#sort descending by key
items.sort(reverse=True)
print(items)

print(dict(items))

#the above works because sorted/.sort will sort by the first thing it finds in the tuple unless they are the same, but they will never be the same because this is a dictionary


#lambda function in python are just anonymous functions in python
#sort ascending by value

#without lambda. e is the tuple
def get_key(e):
    #return that we want to sort by
    return e[1]
items.sort(key=get_key)

print(items)


#same but using a lambda function
items.sort(key=lambda e: e[1])
print(items)


#count number of letters in a string

def print_letter_count(s):
    counts = {}
    #c = c.lower() to make case insensitive
    for c in s:
        if c in counts:
            counts[c] +=1
        else:
            counts[c] = 1

    items = list(counts.items())
    items.sort(key=lambda e: e[1])
    print(items)

print_letter_count("aaabbcbca")


#Caesar Cipher

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

def encode(s):
    r = ""
    for c in s:
        if c in encode_table:
            r += encode_table[c]
        else:
            r+=c
    return r

decode_table= {}

#dictionary comprehension would also work
# decode_table = {value: key for key, value in encode_table.items()}
def build_decode_table():

    for key in encode_table:
        value = encode_table[key]
        decode_table[value] = key

    # for key, value in encode_table.items():
    #     value = key
build_decode_table()

def decode(s):
    r = ""
    for c in s:
        if c in decode_table:
            r += decode_table[c]
        else: r+=c
    return r

