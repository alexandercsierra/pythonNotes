table_size = 8
hash_table = [None] * table_size

def myHash(key):
    str_bytes = key.encode()
    total = 0

    for letter in str_bytes:
        total+=letter

        # #32 bit 8 f's
        # total&= 0xffffffff
        # #64 bit 16 f's
        # total&= 0xffffffffffffffff

    return total % table_size

def insert(key, value):
    index = myHash(key)

    hash_table[index] = value


def get(key):
    return hash_table[myHash(key)]

def delete(key):
    hash_table[myHash(key)] = None


insert('blue', 'favorite')
insert('green', 'okay')
# print(hash_table)
delete('blue')
# print(hash_table)

# print(get('blue'))

#implement a hashtable class and hashtableentry class
#use a good hashing function
    #implement eight DJB2 or FNV-1(64-bit)
#implement the hash_index() that returns an index value for a key
#implement the put() get() and delete() methods



#Class Notes

#if you had to search through 1000 blocks to find just one, it would be O(n)

#if you sorted them, you could do O(logn) because you could do binary search, throwing away half of the calculations with each step

#If you wanted it to be any better, you would use a hashtable (dictionary in python)


"""

"amet" -> [magic box] -> 4
"ipsum" -> [magic box] -> 1

magic box where the word itself gives you the index where it should be stored in a list

"""

data = [None] * 8


"""
"beej" -> hashing_function() -> some index
"""
#good hashing functions are deterministic (same input gives same output) and has minimal collisions. Space complexity will be O(n) if no collisions

#with big O notation, n is the number of slots in data. Number of bytes is different. Looping over the bytes of the key is O(n) but it is not technically the input so still O(1). Since keys tend to be samll, it can be ignored.
def my_hashing_function(s):
    string_bytes = s.encode()
    total = 0
    for b in string_bytes:
        total+=b
    
    return total

#mod the hashed value to make sure that the returned hash will exist as an index in the data list, otherwise it might be too large
def get_slot(s):
    hash_val = my_hashing_function(s)
    return hash_val % len(data)

print(my_hashing_function('beej'))


def put(key, value):
    slot = get_slot(key)
    data[slot] = value

put('beej', 3490)
print(data)


def get (key):
    slot = get_slot(key)
    return data(slot)

def delete(key):
    put(key, None)


#hash tables vs binary search tree - don't have to worry about collisions in a binary search tree, and also you don't have to allocate more memory than you need (like we did above multiplying a list by some number)


