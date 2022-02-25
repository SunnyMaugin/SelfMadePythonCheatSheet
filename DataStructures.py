# LISTS

letters = ["a", "b", "c"]
number = [1, 2, 3, 4]
matrix = [[0, 1], [0, 2]]   # a list within a list
zeros = [0] * 100   # if you need a very long list you can multiple to create a big list instead of typing it out all manually
combined = zeros + number  # you can concatenate list together which mean combine them together
numbers = list(range(20))   # this will create a list from 0 to 20 but not including 20 and this just makes it easier and cleaner to read and type 
chars = list("Sunny Maugin")    # this function is not limited to integers only but can turn a string into a list with all its single characters

# Easily reverse a list

numbers = list(range(20))
print(numbers[::-1])    # this means from start to end print numbers starting from the end of the list and down and if it was [::2] we would print every second element in he list


# LIST UNPACKING

numbers = [1, 2, 3]
first, second, third = numbers  # this line of code is the same as the 3 lines below and this is list unpacking you can see why its better, there needs to be a variable for each value otherwise an error will be shown
first, *other, last = numbers # if you have a big list and only care about a few numbers you can get the values and then store the rest in another big variable with *other

first = numbers[0]
second = [1]
third = [2]


# LOOPING OVER LISTS

nums = [1, 2, 3, 4]

for num in nums:    # this would output every element in the list
    print(num)

nums = [1, 2, 3, 4]

for num in enumerate(nums):    # however using enumerate you can create and store each element inside a tuple with its index position, for example 1 would output ---> (0, 1), index will be first then value
    print(num)
    print(num[0], num[1])   # if you only wanted the indexes you could use num[0] and num[1] for only values, ALSO doing it this way makes the output not a tuple

nums = [1, 2, 3, 4]
# using index, num you are unpacking the tuple that is created with enumerate
for index, num in enumerate(nums):    # this is a better way to achieve the same result without having to restrict the output into tuples
    print(index, num)   


# ADDING/REMOVING ITEMS

# Add
letters = ["a", "b", "c"]
letters.append(1, "d") # using list methods you can do various things to a list, in this example you can append a value to a list
letters.insert(1, "a1") # this will allow you to append a value to the list but insert it anywhere you like

# Remove
letters.pop(0)   # this method will "pop" remove the last item in the list if has no argement, however you can insert an index position you would like to remove, in this case "a" would be removed
letters.remove("c") # this method can be used to remove any value you want from the list if you dont know where it is, but if you have multiple "c"'s you want to remove then you will have to run a loop over this statemnt
letters.clear() # this method is used if you want to remove everything in the list
del letters[:2] # this can be used if you want to remove a certain section of the list, in this case it would remove elements from index 0 to but not including 2

# Finding item in a list

letters = ["a", "b", "b", "c"]
print(letters.count("b"))  # you can use the method count to count the amount of occurences a value has inside a list
if "d" in letters:
    print(letters.index("d"))   # using the index method you can print out the index of a certain value if exists inside the list, in this case it would throw out an error because d doesnt exist


# SORTING LISTS

numbers = [5, 7, 2, 6, 3]
numbers.sort()   # this method will sort the list into ascending order
number.sort(reverse=True) # you can pass an arguements reverse inside the sort method and make it true to sort the list in descending order
sorted(numbers, reverse=True) # unlike the statements above this will not change the original list but create a new one and sort that list into ascending or decending order using revers, output = 1 sorted list and the original list


# LAMBDA FUCTIONS

# A way to sort a list with tuples inside, with normal sort method it wont work
products = [
    ("Product 1", 2.90),
    ("Product 2", 1.99),
    ("Product 3", 11.99)
]

products.sort(key=lambda product: product[1])
print(products)


# MAP FUNCTION

# using a map function you can output all the prices of the products more cleaner and easily instead of writing 4-5 lines of code
products = [
    ("Product 1", 2.90),
    ("Product 2", 1.99),
    ("Product 3", 11.99)
]

prices = list(map(lambda product: product[1], products)) # OUTPUT ---> [2.90, 1.99, 11.99]


# FILTER FUNCTION

# the filter function is used to filter aout the values in a list, fore example to only print the products with the value that is greater or equal to 5
products = [
    ("Product 1", 2.90),
    ("Product 2", 1.99),
    ("Product 3", 11.99)
]

filtered = list(filter(lambda product: product[1] >= 5, products))
print(filtered)


# LIST COMPREHENSTION

products = [
    ("Product 1", 2.90),
    ("Product 2", 1.99),
    ("Product 3", 11.99)
]

prices = list(map(lambda product: product[1], products))
prices2 = [product[1] for product in products]   # this statement is exactly the same as the one above but its easier to read and simpler
print(prices2)

# same goes for the filter function

filtered = list(filter(lambda product: product[1] >= 5, products))
filtered2 = [product for product in products if product[1] >= 5]
print(filtered2)


# ZIP FUNCTION

# the zip unction is used to combine 2 lists together into tuples for example:
list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(zip(list1, list2)) # using the ZIP function it would output ---> [(1, 10), (2, 20), (3, 30)]
print(zip("ABC", list1, list2)) # this would output ---> [("A", 1, 10), ("B", 2, 20), ("C", 3, 30)]


# STACKS - LIFO (Last In First Out)

# this is the stack concept in python
browsing_session = []   # this is the users browse session currently empty
browsing_session.append(1)  # he visits 3 sites
browsing_session.append(2)
browsing_session.append(3)
browsing_session.pop()  # he backspaces from the site last in 
if not browsing_session:    # check if the browsing session is not empty, if it isnt then print the last session he visited
    browsing_session[-1]
else:
    print("no results found")


# QUEUES - FIFO (First In First Out)

# queues concept in python
from collections import deque
queue = deque([])   # using deque, you can pass a list as an arguement and create a queue
queue.append(1) # then we append some elements to represent a real queue, for example who is nect at the till
queue.append(2)
queue.append(3)
queue.popleft() # this method will remove the furthest left element meaning the first element in the list , however it can only be used on lists using deque otherwise this wont work
if not queue:   #   then we check if the queue is empty if it is the print "empty"
    print("line is empty")


# TUPLES

# tuples are useful when you have values that should not change so to prevent accidental changes to it, turning it into a tuple will reduce risk of accidently adding or removing or messing with the list
# a tuple is a read-only list
coords = (2, 6) # this is a tuple however
coords = 2, 6   # python will aslo read this as a tuple, these 2 lines or exactly the same
coords = 2  # this will not be a tuple just a normal value, however
coords = 2, # now python will regognise this as a tuple
coords = () # and this is how you define an empty tuple

coords = (2, 6) + (0, 4)    # just like lists you can concatenate(combine) tuples together or multiply them, OUTPUT ---> (2, 6, 0, 4)

coords = tuple([2, 6])  # using the tuple function you can turn a list into a tuple, you can also turn a tring into a tuple as strings are iterable
print(coords)

# tuples are a read-only list, but you are still able to access certain elements and unpack the tuple
coords = (2, 6)
print(coords[1])
if 6 in coords:
    print("exists")


# SWAPPING VARIABLES

x = 10
y = 20

x, y = y, x # this is swapping variables which allows us to set different values to the same variable with writing a lot of lines, its the same as unpacking a tuple
a, b = 1, 2 # this is unpacking a tuple you create a tuple and assign it variables in the same line and avoid creating a tuple and then defining lots of variables under and repeating code, example:

coords = (1, 2)
a = coords[0]       # this is the same as a, b = 1, 2
b = coords[1]


# ARRAYS


