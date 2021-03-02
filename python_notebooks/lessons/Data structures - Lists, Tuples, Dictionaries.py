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

# # Lists

# Lists are a very useful data type that can be thought of as collections of separate variables of any type.  They are generated using square brackets.

values = [1,2,3,4]
print(values)
print(type(values))
print(len(values))

# The `range( )` function is a useful way to generate a list of numbers.  The notation is range(start,stop,step).  What will the last number in this list be?

values = list(range(1,10,1))
print(values)
values = list(range(10))
print(values)
values = list(range(0,10,2))
print(values)

values = range(0,10,2)
print(*values)

# #### Indexing

# Lists index and slice like strings, starting at 0.  Lists can be indexed in reverse.

values = list(range(1,5,1))
last = len(values)-1 # correct for indexing starting at 0
print(values)
print(values[2])
print(*values[1:])
print(values[-1])
print(values[last])

# #### Changing lists

# Unlike strings, lists are mutable (that is, they can be changed).

values = list(range(1,5,1))
print(values)
values[0] = 0
print(values)

# Lists can be expanded using addition and multiplication operators.

values = list(range(1,5,1))
print(values + values)
print(values*3)

# Lists can be appended (single item) or extended (with another list) using [list methods](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) `.append()` and `extend()`.

# +
values = list(range(1,5,1))
print(values)
values.append(5)
print(values)

values2 = list(range(6,9,1))
values.extend(values2)
print(values)
# -

# List items can be removed or inserted.

values = list(range(1,5,1))
print(values)
values.remove(2)
print(values)
values.insert(0,2) # .insert(position, item)
print(values)

# List items can be sorted, or reversed.

values = list(range(1,5,1))
print('The starting list is: {0}'.format(values))
values.extend(values)
print('The extended list is: {0}'.format(values))
values.sort()
print('The sorted list is: {0}'.format(values))
values.reverse()
print('The sorted list in reverse is: {0}'.format(values))

# Calling the `.sort( )` method changes the list.  Using the `sorted( )` function does not.

# +
values = list(range(1,5,1))
print('The starting list is: {0}'.format(values))

values.extend(values)
print('The extended list is: {0}'.format(values))

new_list = sorted(values)
print('The output of the sorted function is: {0}'.format(new_list))
print('The extended list hasn\'t changed: {0}'.format(values))

values.sort()
print('The sort method changes the list: {0}'.format(values))
# -

# Setting a variable to equal a list does not make a copy of that list.  Changing an item will change it in both lists! 

values = list(range(1,5,1))
print(values)
mirror  = values
mirror[0] = 0
print(mirror)
print(values)

# To make a copy of a list, you can use slicing.

values = list(range(1,5,1))
copy = values[:]
copy[0] = 0
print(copy)
print(values)

# In many instances you want to break down a string into separate varaibles and then do something to them.  The `.split( )` method will break up a string into a list.

fish = 'Danio rerio'
names = fish.split()     #splits at white space by default
print(names)
fishes = 'Oryzias latipes,Danio rerio,Takifugu rubripes'
names = fishes.split(',')  #can split at commas, tabs, etc.
print(names)
names.sort()
print(names)
print(names[0])

# The index method will search a list and return the index position of the found item. See help for additional parameters taken by `.index( )`.

fishes = ['Oryzias latipes','Danio rerio','Takifugu rubripes']
print(fishes.index('Danio rerio'))

# +
# list.index?
# -

# `.count( )` will return the number of instances of an item in a list.

fishes = ['Oryzias latipes','Danio rerio','Takifugu rubripes','Danio rerio']
print(fishes.count('Danio rerio'))

# # Tuples

# Tuples, like lists, are collections of items that are indexed.  However unlike lists they are immutable. They are defined by parentheses.

items = (1,2,3,'string 1',2)
print(len(items))
print(items[1:])
print(items.index('string 1'))
print(items.count(2))

# The `list( )` and `tuple( )` functions can change collections of items.

items = [1,2,3,'string 1',2]
items_t = tuple(items)
print(items)
print(items_t)
items_l = list(items_t)
print(items_l)

# Uisng `zip( )` to combine lists into a list of tuples.

genus = ['Oryzias','Danio','Takifugu']
species = ['latipes','rerio','rubripes']
fishes = zip(genus,species)
print(list(fishes))

# # Dictionaries

# Dictionaries are data structures used as lookup tables.  Items are joined as key:value pairs, but are not inherently ordered.  Dictionaries are defined by curly brackets `{ }`.  They are unordered structures, so cannot be indexed by position or sliced.  They are a very fast way access data.  Dictionary values can be numbers, strings, tuples, lists or any combination.

# +
tanks = {'1215':'AB', '1183':'brn3c:gfp','1941':'myo6:gfp'}

print(tanks['1183'])
# -

# Adding and deleting dictionary entries

tanks = {'1215':'AB', '1183':'brn3c:gfp','1941':'myo6:gfp'}
print(tanks)
tanks['1222'] = 'myo6:nls-eos'
print(tanks)
del tanks['1183']
print(tanks)

# A list of tuples can be converted into a dictionary using `dict( )`

numbers = ['1215','1183','1941']
stocks = ['AB','brn3c:gfp','myo6:gfp']
tanks = zip(numbers,stocks)
print(dict(tanks))

# All keys and values can be accessed using dict methods.

tanks = {'1215':'AB', '1183':'brn3c:gfp','1941':'myo6:gfp'}
print(tanks.keys())
print(tanks.values())
print(tanks.items()) #returns list of key:value tuples

# `dict.get` will return the value for the given key, or the designated alternative.  If the alternative is not defined, it defaults to None

tanks = {'1215':'AB', '1183':'brn3c:gfp','1941':'myo6:gfp'}
print(tanks.get('1215','empty tank'))
print(tanks.get('1216','empty tank'))

# Dictionaries can be combined using `update( )`. New key:value pairs are added and existing keys are updated to new values.

tanks = {'1215':'AB', '1183':'brn3c:gfp','1941':'myo6:gfp'}
new_tanks = {'1215':'sputnik', '1281':'sost:nls-eos'}
print(tanks)
tanks.update(new_tanks)
print(tanks)
