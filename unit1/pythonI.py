#UPER
#understand
#plan
#execute
#reflect


#Programming vs. Investigative Journalism

# String interpolation
print(f”hello {name}”)

# backticks don’t count as quotes

# while in python repl type help(thingIwanthelpwith) and will bring up info

# No const/var/let equivalent

# python strings are immutable
# the original string isn’t changed
# if it appears changed, it’s just been replaced with the new value
# could not for example change str[0] = “B”
# reassigning the variable as a whole is ok,
name = “will”
name = “bill”
# but actually changing the string not ok
str[0] = “B”
# referencing a different memory location instead of changing data in the old memory address
# the string is immutable, but the variable isn't
# the container is mutable, but the data is not
# you can't alter it, but you can overwrite it with something else

# Python has garbage collection
# finds memory not being used anymore
# frees it up
# reference counting
# memory knows how many things are looking at it
# everything has a reference count
# RC is 1 if name is only thing references will
# if RC is 0, deletes them



# is compares the identities of the objects, == compares the values of the two objects
# “is” is the same as === 
#  The is keyword is used to test if two variables refer to the same object. The test returns True if the two objects are the same object. The test returns False if they are not the same object, even if the two objects are 100% equal.
# is checks if they are the same object. name and name2 are different objects.
id(id(name)) != id(name) 
# therefore the response to ID is its own object, and therefore the responses aren’t the same object


# The ids themselves, when created are stored in two different locations in memory, so they would not be equal using “is” even if the numbers are the same, because one is the id of name and one is the id of name2



# Lists
.push() 
# is now 
.append()


# loop through with indices
for index in range(len(	q)):
	do a thing with q[index]

# or 
# starts at zero, does not include len(q) similar to i<q.length
for index in range(0, len(q)):
	do a thing with q[index]

# loop through every element
for item in myList:
	do a thing

# gives both elements and indices
for (i, x) in enumerate(myList):
	print(i, x)


# Dictionaries
# object equivalent
# assoc keys with values
# numbers can be used as keys
# dot notation does not work
# need to use square brackets

# iterate through dict


# k is the key
for k in e:
	#prints key then value
	print (k, e[k])


for k,v e.items():
	#prints key then value:
	print (k, v)

# could also do 
for v in e.values()

# or 

for k in e.keys()

# List Comprehensions

evens = [2,4,6,8,10]
evens = [i for i in range(11) if i%2 ==0]

# above same as below
for i in range(11):
	if i%2 == 0;
		evens.append(i)

range(2,11,2) 
# would skip by 2 instead of 1 each time

# the first i is sort of shorthand for the append

evens1 = [0,2,4,6,10]

#dict where the keys are int indices with values as even numbers
#enumerating gives keys and values
d = {i:x for i, x in enumerate(evens_1)}

# could also flip keys and values d={x:i…}

	

