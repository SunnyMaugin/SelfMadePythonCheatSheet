# HANDLING EXCEPTIONS

# using the try and except statements you can output a message in case the block of code under "try" recieves an error
try:
    age = int(input("Age: "))
except ValueError:  # this means whenever the code above or under the try statement runs into a valueerror to run the code below the except statement
    print("Please enter a valid age")


# HANDLING DIFFERENT EXCEPTIONS

try:
    age = int(input("Age: "))
    xfactor = 10 / age
except ValueError:  
    print("Please enter a valid age")
except ZeroDivisionError:   # you can add more acceptions so that your program eill not crash because of errors
    print("Age cannot be 0")

# However if you wanted to display a error message for 10 different errors writing this 10 times would be ugly and take time

try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError): # you can add them in one except statement as arguements and print out the same error message for all errors  
    print("Please enter a valid age")