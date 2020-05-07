a = [1,3,4,5,6]

#points to same location in memory as a
b = a 
#creates a new copy of a and stores it in b
b = a[:]

#fp stands for "file pointer"
#not quite the same as assigning to a variable
#inside of fp are all of the different lines of content
#can iterated through it
#with automatically closes the file
with open("foo.txt") as fp:
    for line in fp:
        print(line)


fp = open("bar.txt", "w")
fp.write("Write stuff")
#closing the file will free up resources and stop possible data loss from the written content not having migrated from RAM to HD fast enough
fp.close()

with open('bar.txt', 'w') as f:
    f.write('Python\n')
    f.write('JavaScript\n')
    f.write('Angular\n')
f.close()

#put in method that lives in player class
attribute = direction + "_to"
if hasattr(curr_room, attribute):
    getattr(curr_room, attribute)