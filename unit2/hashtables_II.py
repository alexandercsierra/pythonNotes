#bar and baz hash to same slot

class HashTableEntry:
    def__init__(self, key, value):
    self.key = key 
    self.value = value 
    self.next = None

"""
PUT
Find the slot for the key
search linked list for the key
    if found update it
    if not found, make a new hashtable entry and add to the head of the list


GET
Find the slot for the key
search linked list for the key
    if found, return the value
    if not found, return None

DELETE
Find the slot for the key
search linked list for the key
    if found, delete it from the linked list then return the deleted value
    if not found, return None
"""


#Hash Table Load Factor
#load factor is number of things stored in the hashtable / number of slots in the array

#8 slots and 8 elements => 8/8 => load factor: 1.0

#don't want to count all items 
#increment count of items at any given time


#Resize
"""
allocate new array of bigger size
traverse old hash table -- O(n)
    for each element figure out it's slot in the new, bigger array
    put it there


don't want to resize super frequently because it's an O(n) operation. This is why the typical resize is to double it.
"""

