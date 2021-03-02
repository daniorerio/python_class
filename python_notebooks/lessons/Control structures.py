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

# # Control structures

# ### Evaluation statements

# Many programs compare conditions and then execute a set of instructions.  There are several types of comparators.  The output of these statements is a boolean variable (`True` or `False`).

# +
#equality comparisons
print(5==5)
print(3==5)
# not equal
print(5!=5)
print(3!=5)

# less, greater, less or equal
print(5<5)
print(3>5)
print(5<=5)

# +
#string comparisons

print('danio' == 'danio')
print('Danio' == 'danio')
genus = 'Danio'
print(genus == 'Danio')
print(genus == 'danio')
print(genus.lower() == 'danio')
# -

# The `in` operator tests whether an item is in a list of values.

# item in a list
values = range(1,5,1)
i = 2
j = 5
print(i in values)
print(j in values)

# The `in` operator can als be used to test whether a key is in a dictionary.

tanks = {'1215':'AB', '1183':'brn3c:gfp','1941':'myo6:gfp'}
print('1215' in tanks)
print('1216' in tanks)

# ### If statement

# The `if` statement executes when comparison is true.  The `if` statement must be followed by a colon.  All indented lines immediately following the `if` statement are executed. 

# +
Uber = 10.00
Metro = 2.50
cash = 1.50

if Uber < cash:
    print('I can get a ride')
    
if Metro < cash and Uber > cash:  # can use and, or for multiple comparisons
    print("I'll take the bus")
    
if Metro > cash:
    print('Walking...')

# -

# Multiple `if` statements can be written to parse a number of conditions using `elif` (else if) and `else`.  Colons are needed.

# +
Uber = 10.00
Metro = 2.50
cash = 1.50

if Uber < cash:
    print('Enjoy your car ride')
elif Metro < cash:
    print('Another one rides the bus')
else:
    print('Walking...')
# -

# ## Loops

# Loops allow repetition of statements.  `for` and `while` provide control to loops, so that statements are iterated for a defined number of times. Colons are needed after the `for` or `while` statement.  Indented statements are performed in order after the loop statement.

# ### For loop

# For loops iterate over a collection of objects, completing the loop a defined number of times. For loops take the form for variable in range of variables.  The variable (often i by convention) can be used as a counter.
#
# The `range` function can use several conventional terminologies.

for i in range(1,5):
    print(i)
print ('\n')
for i in range(5):
    print(i)

# A `for` loop can also iterate over all the values in a list using the following terminology. In the first example the step function in `range( )` makes the list more than a simple range of counters.  How many times will this loop be executed?

#iterate over a list
values = range(0,11,2)
for i in values:
    print (i)

#iterate over a list
fishes = ['Oryzias latipes','Danio rerio','Takifugu rubripes']
for fish in fishes:
    print (fish)

# You can use the `range(len(variable))` notation when you want to capture the iterator number.

# +
#iterate over a string
zfish = 'Danio rerio'

for i in zfish:
    print(i)

print (range(len(zfish)))

for i in range(len(zfish)):
    print(i,zfish[i])
# -

# `enumerate` gives back both index and value from a list, allowing additional flexibility in loops.

# +
fishes = ['Oryzias latipes','Danio rerio','Takifugu rubripes']

index = 0
for fish in fishes:
    print(index, fish)
    index += 1
    
#or you could do it this way

for i, fish in enumerate(fishes):
    print(i, fish)

# +
# enumerate?
# -

# Continue and break statements give some control over iteration within a loop.  The `continue` statement moves to next line in a loop.  `break` stops a loop.  These are also useful in debugging code.

for i in range(10):  
    print(i, i%2) # modulus function gives remainder of integer division
    if i % 2:
        continue
    print("Even number")

for i in range(10):
    if i == 5:
        break
    print (i)

# ### Loops within loops

# Having a second loop within a first loop is common in programming.

for i in range(4):
    for j in range(3):
        print('i: {0} j: {1}'.format(i,j))
    print('end inner loop')
print('end outer loop')

# ### While loop

# The while statement does something as long as condition is true.  This is useful if the number of iterations of a loop is not known ahead of time.  Below, count could be any number to start.

# +
count = 10

while (count >0):
   print (count, end=" ") #end = " " replaces the default newline after print
   count -= 1
# -

# Sometimes you want to do something without specifically evaluating a condition at the beginning of the loop.  You can use `while True` to do this.

# +
x = 'abcabc'
search_var = 'b'

count = 0
loc = 0

while True:
    loc = x.find(search_var,loc)
    if loc == -1:
        break
    count += 1
    loc += 1

print('The number of occurrences of {0} in {1} is {2}.'.format(search_var,x,count))

# -

# # List Comprehension

# Python often uses a syntax called list comprehension.  It is not necessary to use it but it is common, so you should become familiar with it.  It takes the following syntax:

# `list = [expression for member in iterable]`

# The input can be a list or other iterable structure.  The expression modifies the input, resulting in an output list.

squares = [i * i for i in range(10)]
print(squares)

# Here is how to use list comprehension to replace a `for` loop.

# +
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#standard way

new_list = []
for x in my_list:
   new_list.append(x * 2)

print(new_list)
    
#using list comprehension

new_list = [x * 2 for x in my_list] # square brackets enclose list comprehension statement

print(new_list)
# -

# In addition you can use a conditional statement in the list comprehension syntax.

# +
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# generating a list of even numbers converted into string variables, standard way

new_list = []
for x in my_list:
   if (x % 2) == 0:
     new_list.append(str(x))
        
print(new_list)

# using list comprehension

new_list = [str(x) for x in my_list if (x % 2) == 0]

print(new_list)
# -

# Similarly you can use dictionary comprehensions to produce dictionaries, replacing `[ ]` with `{ }` in the comprehension syntax.

squares = {i: i * i for i in range(10)}
print(squares)
print(squares [4])


