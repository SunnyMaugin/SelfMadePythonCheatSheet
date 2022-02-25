# DEFINING A FUNCTION
def greet():    # defining the function using def and all the code writtin inside this function will run once the function is called
    print("Hello")
    print("Welcome to VSCODE!")


greet() # calling the function


# PARAMETERS & ARGUEMENTS

def greet(first_name, last_name):   # these are called parameters
    print(f"Hello {first_name} {last_name}")
    print("Welcome to VSCODE!")


greet("Sunny", "Maugin")    # the actual values of the parameters are called arguements 


# DIFFERENT FUNCTIONS

# above was a more simpler function you couldnt reuse properly, for example write to a file or send over email but using this function you can
def greet(name):
    return f"Hello {name}"


message = greet("Sunny Maugin")
file = open("greet.txt", "w")
file.write(message)
# using this type of function using return you are returning a value which allows you to do anyhting with it


# DEFAULT ARGUEMENTS

# if one of the function parameters do not have a value then you can set a default value inside the parameters so that even if the parameter isnt given a value then the default value will be x
def sum(number, by=1):  # when calling our function you can see we haven't given 'by' a value and normally will give us an error however in the parameters by=1 which is now its default value
    number * by         # the default value is only used if the parameter value isnt set, also default arguements should always come after the required arguement all defauly arguements come at the end


print(sum(2))


# XARGS

# xargs just means x amount of arguements, for example instead of writing 20 arguements inside the parameters you just use *name and then you can output as many arguements as you want like below
def sum(*numbers):
    total = 0
    for number in numbers:
        total *= number
    return total


print(sum(1, 2, 3, 4, 5))


# XXARGS

# this is the same as xargs, however insead of being able to pass in lots of normal arguements, xxargs allows you to pass in as many KEYWORD ARGUEMNTS as you want
def user(**login_info):
    print(login_info["age"])    # you can access any value by printing its key, so age's value would be 18


print(user(email="hahaha@gmail.com", password="sillystring123", age=18))
# this allows you to make key value pairs and output them inside a dictionary as key value pairs


# FIZZBUZZ EXCERCISE

def fizzbuzz(input):
    if (input % 3 == 0) and (input % 5 == 0):   # moved this expression here otherwise it will print fizz or buzz all the time if its divisble by 3 or 5 and wont get down to this expression
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

print(fizzbuzz(15)) # output: Fizzbuzz