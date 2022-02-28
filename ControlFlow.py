# COMPARISON OPERATORS

#   >   greater than
#   <   less than
#   >=  greater than or equal to
#   <=  less than or equal to
#   ==  the number is equal to
#   !=  not equal too

# can be used on strings and numbers


# CONDITIONAL STATEMNTS

shoe_size = 5

if shoe_size > 5:
    print("Large")
elif shoe_size == 5:    # allows you to add as many if statements as you want
    print("Meduim")
elif shoe_size < 5:
    print("Small")
else:
    print("please enter a number")


# LOGICAL OPERATORS

# and
# or
# not

#example
high_income = True
good_credit = True
student = True

if (high_income and good_credit) and not student:  # using and means it can only be True if both statements are True otherwise its False, "or" would mean if at least 1 is true then its true, "not" just inverses the boolean
    message = "Eligible"
else:
    message = "Not Eligible"


# CHAINING COMPARISON OPERATORs

age = 22
if 18 <= age < 24:  # this means that if age is between 18 and 24 including 18
    message = "eligible"


# FOR LOOPS

for number in range(3): # The range function just repeats something x amount of times and its argeuemts work as start, stop, step, for example this would just repeat "Hello" 3 times
    print("Hello")

for number in range(1, 7, 2): # This would print 1 to 7 in steps of 2 ---> 135, number is the index position 
    print(number)

# FOR ELSE LOOP

successful = True
for number in range(3): # this is a "for else" loop 
    print("Hello")
    if successful:
        print("attempt successful")
        break
else:   # this means that if we complete the for loop completely then the else is printed, however if we dont loop through the for loop fully then it wont be printed
    print("sorry we tried")


# NESTED LOOPS

for x in range(5):  # this is a nested loop which contains a loop inside a loop which is useful for certain algorithms
    for y in range(5):  # the second loop will loop through the input after each check from the first loop, in short the second loop will print all the combinations with 1 from the first loop up to 5
        print(f"{x}, {y}")

""" output: x  y
            0, 0
            0, 1
            0, 2
            0, 3
            0, 4
            1, 0
            1, 1
            1, 2
            1, 3
            1, 4
            2, 0
            2, 1
            2, 2
            2, 3
            2, 4
            3, 0
            3, 1
            3, 2
            3, 3
            3, 4
            4, 0
            4, 1
            4, 2
            4, 3
            4, 4    """


# WHILE LOOPS
# we use while loops to loop a piece of code whilst something is true or false for example:

number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":    # you can use .lower to ensure that no matter what way quit is written, it will quit the program
    command = input(">>>")
    print("ECHO", command)

# EXCERSISE
# OUTPUT all even numbers from 1 to 10 then print the amount of even numbers found
even_num = 0
for num in range(1, 10):
    if num % 2 == 0:    # using the modulus operator so that i can check if the number has a remainder after dividng it by 2 it means its odd, if its equal to 0 then its odd
        even_num += 1
        print(num)

print(f"We have {even_num} even numbers")

#SUCCESSFUL
