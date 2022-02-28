

# MEMOIZATION


"""  Memoization is when you have a program and it saves the answers to the previously already calculated operations into a cache, for example the sum of a number inputed every 2 seconds 
with a message, if the number being inputed comes up more than once then thats where memoization is useful, because instead of doing the same calculation again and using more memory to store
the result, it will just remeber and return the same result as the previous operation. """

""" 
EXAMPLE OUTPUT:  

Computing... 2*2 ------
4                      |
Computing... 5*5       |
35                     |
Computing... 2*2  -----> Both these outputs are the same output, the computer did not redo the calculation but take it from memory in cache where it saved the same operation from line 13
4
Computing... 3*4
12
"""

# You can see that for a small program its not saving us a lot of memory, however when working with bigger and larger operations this would come in handy to improve efficiency