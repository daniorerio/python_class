# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Functions

# Writing your own functions allows you to repeat blocks of code without the effort or rewriting the code.

# Functions are defined by `def`.   Function definitions must come earlier than the line where they are called.  The values passed to the function are called arguments. Functions can return a value that can be assigned a variable name.

# + jupyter={"outputs_hidden": false}
def add_two_numbers(number_1,number_2):  # colon required
    new_number = number_1 + number_2
    return new_number

answer = add_two_numbers(2,6)
print(answer)


# -

# The `*` notation allows the passage of an undefined number of arguments.

# + jupyter={"outputs_hidden": false}
def add_numbers(*numbers):
    new_number = 0           # new_number needs to be defined in order to add to it later
    for num in numbers:
        new_number += num
    return new_number


print(add_numbers(2,4))
print(add_numbers(2,4,6))
print(add_numbers(2,4,6,8))

answer = add_numbers(2,4,6,8)
print(answer+2)


# -

# Functions can return multiple values as tuples or be individually assigned to variables.

# + jupyter={"outputs_hidden": false}
def summary_stats(*numbers):
    num_sum = 0           # new_number needs to be defined in order to add to it later
    for num in numbers:
        num_sum += num
    num_mean = num_sum/len(numbers)
    return num_sum,num_mean

answer = summary_stats(2,4,6,8)
print(answer)
out_sum,out_mean = summary_stats(2,4,6,8)
print(out_sum)
print(out_mean)


# -

# ### Local variables

# Variables created inside a Python function only exist inside that function. Only values defined by the function call and return are used globally.

# + jupyter={"outputs_hidden": false}
def convert_lbs_to_kg(weight_lbs):
    weight_kg = weight_lbs / 2.20462
    return weight_kg

result = convert_lbs_to_kg(170)

print(result)
print(weight_kg)


# -

# Since the variable `weight_kg` is only defined within the function `convert_lbs_to_kg`, there is an error.

# ### Commenting functions: docstring

# A docstring immediately follows the def statement of a function.  Using triple quotes allows it to span several lines.  The docstring will be called after a help request.

# + jupyter={"outputs_hidden": false}
def center(data, desired):
    '''Return a new array containing the original data centered around the desired value.
    Example: center([1, 2, 3], 0) => [-1, 0, 1]'''
    return (data - data.mean()) + desired

help(center)


# + jupyter={"outputs_hidden": false}
# center?
# -

# ### Errors

# Python will stop running a script if it encounters an error and tries to point out where the error occurred. Try fixing the errors in these functions.

# **Syntax** errors are errors in formatting the code.

# + jupyter={"outputs_hidden": false}
def some_function()
    msg = "hello, world!"
    print (msg)
    return msg


# + jupyter={"outputs_hidden": false}
def some_function():
    msg = "hello, world!"
    print (msg)
     return msg 


# -

# **Name** errors occur when a variable is not defined.  Try fixing the errors in these functions.

# + jupyter={"outputs_hidden": false}
print hello

# + jupyter={"outputs_hidden": false}
for number in range(10):
    count = count + number
print("The count is: " + str(count))

# + jupyter={"outputs_hidden": false}
Count = 0
for number in range(10):
    count = count + number
print("The count is: " + str(count))
# -

# **Index** errors occur when a the index is out of range.  Try fixing the error in this functions.

# + jupyter={"outputs_hidden": false}
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[4])
# -

# **Type** errors occur when the wrong type of variable is used. Try fixing the error in this functions.

# + jupyter={"outputs_hidden": false}
print("The temperature today is: " + 75)


# -

# ### Exceptions

# Python uses exception syntax to avoid errors crashing code.  Use `try:` and `except:` to catch errors.

# + jupyter={"outputs_hidden": false}
def divide_numbers(number_1,number_2):
    try:
        new_number = float(number_1)/number_2
        return new_number
    except (ZeroDivisionError):
        return 'Cannot divide by zero'
    except (ValueError,TypeError):
        return 'Must use numbers'
        
print(divide_numbers(2,4))
print(divide_numbers(2,0)) # gives ZeroDivisionError
print(divide_numbers(2,'b')) # gives TypeError (cannot divide by string)
print(divide_numbers('b',2)) # gives ValueError (cannot convert string to float)


# -

# ### Keyword arguments

# If we use specific argument names in the calling statement, the position of the arguments does not matter.  These are called keyword arguments.

# + jupyter={"outputs_hidden": false}
def divide_numbers(numerator,denominator):
    try:
        new_number = float(numerator)/denominator
        return new_number
    except (ZeroDivisionError):
        return 'Cannot divide by zero'
    except (ValueError,TypeError):
        return 'Must use numbers'

# The function works without using keywords just like above.
print(divide_numbers(2,4))
print(divide_numbers(4,2))

# Using the kewyord names, the order no longer matters.
print(divide_numbers(numerator=2,denominator=4))
print(divide_numbers(denominator=2,numerator=4))

# -

# To accept an arbitrary number of keyword arguments, use **.   This is also a way to pass dictionary data structures to functions.

# Using a variable number of keywords

# + jupyter={"outputs_hidden": false}
def tank_inventory(**kwargs):
    for key, val in kwargs.items():  # items() unpacks individual key:value pairs
        print('{1} is in {0}.'.format(key,val))
    # This function does not return anything
    
tank_inventory(tank_1215 ='AB', tank_1183 ='brn3c:gfp',tank_1941 ='myo6:gfp')


# -

# Using a dictionary to pass arguments:

# + jupyter={"outputs_hidden": false}
def tank_inventory(**kwargs):
    for key, val in kwargs.items():  # items() unpacks individual key:value pairs in a dict.
        print ('{1} is in tank {0}.'.format(key,val))
    
tanks = {'1215':'AB', '1183':'brn3c:gfp','1941':'myo6:gfp'}
tank_inventory(**tanks)  #need to include ** to indicate an object of kwargs


# -

# ### Defining default variables using keywords

# The value of keyword variables becomes apparent when the function uses default variables.  Including default variables in the function definition will allow a function to usually run one way, but allow its behavior to be modified.

# + jupyter={"outputs_hidden": false}
def case_print(test_string, uppercase = False):
    if uppercase == False:
        print(test_string.lower())
    else:
        print(test_string.upper())

case_print('danio')  
case_print('danio', uppercase = True)   
# -

# # Anonymous functions: lambda, filter and map

# Python has a number of structures that allow you to generate anonymous functions on the fly.

# ### lambda

# `lambda` takes the following syntax:  `lambda argument(s): expression`

# +
remainder = lambda num: num %2

print(remainder(5))

# +
product = lambda x,y: x*y

print(product (2,3))
# -

# You can use conditional statements with `lambda` functions:



# ### Filter

# The `filter( )` function uses a `lambda` function to parse a list, following the syntax `filter(object, iterable)`.  The `object` is a `lambda` function that returns a boolean value.

# +
numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

filtered_list = list(filter(lambda num: (num > 7), numbers_list))

print(filtered_list)
# -

# ### Map

# The `map()` function is another built-in function that takes a function object and a list. The syntax of map function is as follows:
#
# `map(object, iterable_1, iterable_2, ...)`



# # Standard operations as functions

# The [operator](https://docs.python.org/3/library/operator.html) module exports a set of efficient functions corresponding to the intrinsic operators of Python.  The functions perform object comparisons, logical operations, mathematical operations and sequence operations.

# +
from operator import *

a = -1
b = 5.0
c = 2
d = 6

print('a =', a)
print('b =', b)
print('c =', c)
print('d =', d)

print('\nPositive/Negative:')
print('abs(a):', abs(a))
print('neg(a):', neg(a))
print('neg(b):', neg(b))
print('pos(a):', pos(a))

print('\nArithmetic:')
print('add(a, b)     :', add(a, b))
print('mod(a, b)     :', mod(a, b))
print('mul(a, b)     :', mul(a, b))
print('pow(c, d)     :', pow(c, d))
print('sub(b, a)     :', sub(b, a))
print('truediv(a, b) :', truediv(a, b))
print('truediv(d, c) :', truediv(d, c))
print('floordiv(a, b):', floordiv(a, b))
print('floordiv(d, c):', floordiv(d, c))

# +
from operator import *

a = 1
b = 5.0

print('a =', a)
print('b =', b)

funcs = (lt, le, eq, ne, ge, gt)

for func in funcs:
    print('%s(a, b):' % func.__name__, func(a, b))  # __name__ is the variable name
# -




