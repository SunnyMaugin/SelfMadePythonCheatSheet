# STRINGS

course = "Python Programing"
print(len(course))  # getting the length of the input of the variable
print(course[0])    # using the [] brackets to enter an index to find its corresponding value
print(course[-2])   # you can use a negative index number to output of value from the end of the input instead of counting each index up, you can just count down using negative index
print(course[0:3])   # intead of accessing only 1 index you can access multple using SLICING, this expression will print the values starting from index 0 to index 3 but not including 3 so out will = Pyt
print(course[0:6:2])    # you can add a second colon which is step so from index 0 to 6 with a step of 2 so only print every 2 indexes, output = Pto
print(course[:])    # an empty left or an empty right just represents the start of the input to the end meaning this expression will just print out the original input

course = "Python \"Course\" Programming"    # This is an escape sequence meaning python will ignore any character after it, which allows us to use quotes without confusing python and recieving a syntax error
course = "Python  /nProgramming"    # This escape sequence is used to tell python to start a new line from here

first_name = "Sunny"
last_name = "Maugin"
full_name = f"{first_name} {last_name}" # this is an f string and it is used to more easily save memory and make your code clearer to print multiple variable/expressions together
print(full_name)

# methods for strings
course = "Python Programming"
print(course.upper())   # these examples are methods you can use on an object, for example make them all caps or lower case or check if they are all caps or lower case etc.
print(course.isupper())
print(course.lower())
print(course.islower())
print(course.title())   # Capatilises each starting letter of each word, commonly used for names
print(course.strip())   # strips any unessary whitespace from the input, to have a cleaner output
print(course.find("thon"))  # You ca use this method to find where a certain leteer/phrase starts at inside the input
print(course.replace("ming", "mer"))    # allows you to replace an existing letter/phrase with another letter/phrase
print("Pro" in course)  # using 'in' you can check if a letter/phase is in the input or not in this can be useful to check a users login information is valid or not


# NUMBERS
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)  # removes the decimal point, turns it into an integer
print(10 % 3)   # prints out the remainder so 3x3 = 9 1 is left over so OUTPUT = 1
print(10 ** 3)  # this just mean 10 to the power of 3

# built-in functions
import math # you can use the module math and use all of it methods to work with number in a more complex manner
# for a complete list of all the methods for this module here ---> https://docs.python.org/3/library/math.html

print(round(2.7))   # this built in fuction just rounds the number to the nearest whole number
print(abs(-2.56))   # gives the absolute value of a number

# augmented assigned operator
x = 10
x = x + 3
# is the same as
x += 3  # another way to right both lines above in a quicker and cleaner way



