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

# # Introduction to Python Programming: Variables and Math

# ### Functions

# Like mathematical functions, Python functions do something using the objects in the parentheses.  

print("Hello world!")

# ### Comments

# Comments are text used to annotate code. 

# +
#Comments are defined by the number/pound sign.

"""Three quotation marks can be used to define descriptions of following code.  
They are only ignored by the Python interpreter if found at the beginning of the code block."""
# -

# ### Variables

# Variables can be considered containers for values, assigned using the equal sign.  
#
# A value is assigned to a variable name using the equals sign.  On the left hand side of the equals is the name of the variable. On the right hand side is that value that is assigned to it.  The variable name then works just like typing its value.

a = 2
print(a)

# The value of one variable can also be assigned to another variable.

a=2
b=a
print(b)

# ### Types of variables

# Number varibles include integers and floating point numbers.  Boolean variables are True and False.  Text variables are called strings.  The `type( )` function returns the type of variable.

# +
a = 2
b = 1e9
c = False
d = "A string"

print(a)
print(b)
print(c)
print(d)

print(type (a)),
print(type (b)),
print(type (c)),
print(type(d))
# -

# Null values are often used in coding.  The Python null variable is `None`.

value = None
print(value)

# ### Variable assignment

# In Python, variables gain their type automatically by assignment.  Variables can change value by reassignment, as well as change type.

five = 5
six = 6
print(five)
print(type(five))
five = 'five'
print(five)
print(type(five))
five = 'seven'
print(five)

# ### Math

# Integer math is straightforward for addition, subtraction and multiplication.  Guess what the '**' operator does.

five = 5
two = 2
six = 6
print(five+two)
print(five-two)
print(five*six)
print(five/two)
print(five**two)

# In a block of code, reassigning the value of a variable does not change the result of steps already executed. It only changes steps that happen after the reassignment.

a = 5
b = 2
product = a*b
print(product)
a = 2
print(product)
product = a*b
print(product)

# The same variable can be found on both sides of an equals sign. Although conterintuitive from a mathematical perspective, it works because in ccomputer programming the expression on the right hand side of the equation is evaluated first before the variable ont he left is assigned.

i = 1
print(i)
i = i + 1
print(i)

# Iterator notation will add to to a variable and make the sum the new value of the variable.  This is a common bit of code used in many routines.

i += 1
print(i)

# The modulus function provides the remainder after integer division.  While not typically an important function, it is very useful in programming.  It is represented by the `%` symbol.

print(5%2) 

# Variable types can be changed using functions such as `float()` or `str()`.  What do you predict will happen for each of the following?

# +
five = 5

print(five/2)
print(float(five)/2)

print(five*2)
print(str(five)*2)
# -

# ### Modules

# Modules are groups of functions and other code available to use after they are imported.  The [math](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) module has many basic math functions.

import math
five = 5
print(math.cos(five))

# ### Getting help

# To find out what is available in modules, use the `dir( )` function.

dir(math)

# To get help about a single function in Jupyter, use the `?`

# +
# math.pow?
