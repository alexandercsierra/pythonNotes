#List comprehension for [1,2,3,4,5]

# return i from the for loop starting at 1 and ending before 6
y = [i for i in range(1,6)]


#cubes of numbers 0-9

y = [i**3 for i in range(10)]

#uppercase version of the following list
a=['foo', 'bar', 'baz']
y=[s.upper() for s in a]

x=input('enter comma-separated values').split(',')

y=[elem for elem in x if int(elem) % 2 == 0]

print(y)

class Parent:
    def __init__(self, hi, foo):
        self.hi = hi
        
    def foo():
        print('hi')

#separate super for methods?
#can use *kw to substitute for puttin in argmuents that will be unchanged from parent to child
class Child(Parent):
    def __init__(self, *kw):
        super().__init__(hi)
        super().foo

# __repr__ has more flexibility which doesn't have to be a string, but only need __str__ if looking to return as a string

class Latlon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f"{self.lat}, {self.lon}"






#Design a store using OOP methodologies

#what does this store look like?
#what are the attributes we care about?
    #name
    #location
    #categories of products

class Store(LatLon):
    def __init__(self, name, lat, lon, departments):
        self.name=name
        self.location = Latlon(lat, lon)
        self.departments = departments

    def __str__(self):
        return f"Store {self.name}, {self.location}, {self.departments}"

    
store = Store("LambdaStore", 2323, 334, ["clothes"])
print(store)


#we want to add departments

selection = input("Select the number of a department")


#whole file will run on import unless
# if __name__ == '__main__':

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
​
    def __str__(self):
        return f"{self.name} costs ${self.price}"
​
class Department:
    # products with a list of tuples with signature (string, int)
    def __init__(self, name, products=[]):
        self.name = name
        self.products = [Product(*p) for p in products]
​
    def __str__(self):
        return f"No products available in the {self.name} department yet."
​
# what does this store look like?
# what are attributes we care about? 
# a name 
# location 
# categories of products 
# a store needs product 
​
class Store:
    def __init__(self, name, lat, lon, departments):
        self.name = name
        self.location = LatLon(lat, lon)
        self.departments = [Department(d) for d in departments]
​
    # add a __str__ method so that can observe our Store instance 
    def __str__(self):
        return f"Store {self.name}, {self.location}, {self.departments}"
​
store = Store("LambdaStore", 44.13455, -121.123124, ["Clothing", "Cookware", "Books", "Sporting Goods"])
# print(store)
​
# we want to add departments 
# let's take input from the user and have them specify departments by the department's
# index in the departments list  
​
# wrap all this logic in a while loop so that we can keep giving selections
# instead of having re-run the program every time 
while True:
    selection = input("Select the number of a department or type 'exit' to leave: ")
​
    if selection == "exit":
        print("Thanks for shopping with us!")
        break
​
    # add error handling so that when a user inputs a department for a non-existent
    # department, we'll notify them that that department doesn't exist
    try:
        # casting might cause an error
        selection = int(selection)
        if selection >= len(store.departments):
            print("That's not a valid department")
        elif selection >= 0 and selection < len(store.departments):
            print(f"{store.departments[selection]}")
        else:
            print("Department numbers are positive")
    except ValueError:
        # the user didn't give us a value that could be cast to a number
        print("Please enter your choice as a number")
​
    # when should we break out of this loop?
    # let's let the user type "exit" into the selection to have them leave 