# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp
# Exercise 15

# Create pseudocode

# Create a code that define a function
def exponent(base, exp):
    # Creating a code that will calculate the result of the exponent
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
        