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
# lambda is just another way to create a function instead of using "def"
products = [
    ("Product 1", 2.90),
    ("Product 2", 1.99),
    ("Product 3", 11.99)
]

products.sort(key=lambda product: product[1])
print(products)


# MAP FUNCTION

# using a map function is useful for any case where you want to turn a value inside a list and turn into something else
products = [
    ("Product 1", 2.90),
    ("Product 2", 1.99),
    ("Product 3", 11.99)
]

prices = list(map(lambda product: product[1], products)) # OUTPUT ---> [2.90, 1.99, 11.99]


# FILTER FUNCTION

# the filter function is used to filter aout the values in a list, for example to only print the products with the value that is greater or equal to 5
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

# you can use an array instead of a list if you encounter perfromance problems with a huge data using lists
from array import array

numbers = array("i", [1, 2, 3, 4])  # NOTE: the elements inside the list should all be the same data type, for example only intgers not floats or strings etc
numbers[1]  # just like a list you can access any index you want


# SETS

# a set is a list but without any duplicates
# therefore if you wanted to remove all the duplicates from a list you can convert the list into a set
# NOTE: sets are displayed as {} AND do not support indexing so you cannot access an index in a set as they are not ordered, however you can check if an item is in a set
numbers = [1, 2, 2, 3, 1, 3]
unique = set(numbers)
print(unique)   # this would OUTPUT: {1, 2, 3}

# combining two sets which also removes duplicates from both sets and prints them both in one
numbers = [1, 2, 2, 3, 1, 3]
first = set(numbers)
second = {1, 5, 4}

print(first | second) # OUTPUT: {1, 2, 3, 4, 5}
print(first & second) # this would output all numbers in common with the first and second list OUTPUT: {1}
print(first - second) # this will remove all the elements that are common from both sets from the first set OUTPUT: first set = {2, 3}
print(first ^ second) # this will output all the elemants that are in each set but not common in both, OUTPUT: {2, 3, 4, 5} NOTE: only one is common in both


# DICTIONARIES

# ways to write a dictionary
keys = {"x": 1, "y": 2}
keys = dict(x=1, y=2)

# you can add or change (key: value) pairs with
keys["a"] = 3
keys["x"] = 10

# if you want to find/get a value from a dictionary whether you know if it in the dictionary or not you can do
if "z" in keys:
    print(keys["z"])

# OR

print(keys.get("z"))
print(keys.get("z", 0)) # you can set a default value so if the key is not inside the dictionary then it will return its default value you set

# To delete an item from the dictionary you can do

del keys["a"]

# Looping through a dictionary

# if you want to loop and only get the keys then do
for x in keys:
    print(x)
# if you wanted to print the keys and values then you can do
for x in keys:
    print(x, keys[x])   # OUTPUT: x = 10, y = 2
# you can also use unpacking to get the same result
for key, value in keys.items():
    print(key, value)   # OUTPUT: x = 10, y = 2


# COMPREHENTIONS (LISTS, DICTIONARIES, SETS)
# NOTE: VERY USEFUL

values = []
for i in range (5):
    values.append(i * 2)

# this top piece of code is the exact same as this one below:
# NOTE: the syntax for a comprhention is: [expression for item(loop) in items(iterable)]
# NOTE: this is not limted to lists, you can use this for sets and dictionaries

values = [i * 2 for i in range(10)]  # list
values = {i * 2 for i in range(5)}  # set
values = {x: y * 2 for x in range(5)}   # dictionary


# GENERATOR EXPRESSIONS

# generators are used when you are are working with a huge piece of data, using a generator will significantly reduce the amount of memory that is taken
from sys import getsizeof

# generator ---> OUTPUT: gen: 112 (bytes of memory)
values = (i * 2 for i in range(100000)) # using () will turn this staement into a generator and wont work like a comprehention
print("gen:", getsizeof(values))    # OUTPUT: gen: 112 no matter what the size of the input is, NOTE: if we didnt use a generator here then the out putwould be using 800000+ bytes of memory

# list comprehention ---> OUTPUT: list : 824456 (bytes of memory)
values = [i * 2 for i in range(100000)]
print("list:", getsizeof(values))   # OUTPUT: list : 824456


# UNPACKING OPERATOR

# with the unpacking operator you can unpack any iterable, ,eaning you can output each individual element instead of getting [1, 2] as an output you get 1 2
numbers = [1, 2, 3]
print(numbers) # OUTPUT: [1, 2, 3]
print(*numbers) # OUTPUT: 1 2 3

# this piece of code is the same as the code below
values = list(range(5)) # OUTPUT: [0, 1, 2, 3, 4]

# using the unpacking operator you can unpack and combine lists and strings without using built-in functions like list(), dict() etc. NOTE: this is possible because using the unpacking operator it prints out individual characters
values = [*range(5)] # OUTPUT: [0, 1, 2, 3, 4]
values = [*"Hello"]  # OUTPUT: ["H", "E", "L", "L", "O"]
