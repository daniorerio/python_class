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

# # Strings

# [String](https://docs.python.org/3/library/string.html) variables are text.
#
# Strings are created using either single or double quotes. It doesn't typically matter which kind of quotes you use, but they do need to match.
#
# Python 3 uses [Unicode](https://docs.python.org/3/howto/unicode.html) specification for strings (including [emoji](https://home.unicode.org)!).

genus = 'Danio'
print(genus)

# Escape characters are those that would otherwise be interpreted incorrectly by Python.
#
# Escape characters include:
#
# * \\' - Quotation mark
# * \\" - Double quotation mark
# * \t - Tab
# * \n - New line
# * \\\\ - Backslash
#

print ("Danny O\'Rerio")

# Strings can be concatenated.

# +
genus = 'Danio'
species = 'rerio'

full_name = genus + ' ' + species + ' '

print(full_name)
print(full_name*2)
# -

# ### String methods

# [Methods](https://docs.python.org/3/library/stdtypes.html#string-methods) modify variables without changing their values. Methods follow variables using the dot notation.  In many cases the parentheses of methods are left blank.

# +
genus = 'danio'
print(genus)

print(genus.title())

print(genus)

cap_genus = genus.upper()

print(cap_genus)

print (cap_genus.lower())
# -

# White spaces include blank spaces, tabs and the newline character.

full_name = 'Danio rerio '
print(full_name)
tab_full_name = '\t' + full_name
newline_full_name = '\n' + full_name
print(tab_full_name)
print(newline_full_name)

# The `.strip( )` method removes white spaces from either end of strings, but not in the middle.  There are additional methods `.lstrip( )` and `.rstrip( )`.  `.strip( )` is very useful when importing text as it gets rid of white spaces potentially confounding in later code.

tab_full_name = '\tDanio rerio'
print(tab_full_name)
print(tab_full_name.strip())

# ### String formatting

# The `str.format()` method allows the insertion of variable values.  The curly brackets `{ }` indicate the location where the variable should be placed.  More than one variable can be indicated, starting with 0 for the first variable.  What do you think is going to happen with the last line?

genus = 'Danio'
species = 'rerio'
print('The zebrafish is {0}.'.format(genus))
print('The zebrafish is {0} {1}, a common laboratory fish.'.format(genus,species))
print('The zebrafish is {1} {0}, a common laboratory fish?'.format(genus,species))

# ### Indexing strings

# The `len( )` function gives the total number of items within a variable.  With strings, it will return the total number of characters including white spaces.

full_name = 'Danio rerio'
print(len(full_name))

# Indexing will return part of a string.  The index number is included in the square brackets `[ ]`.  In Python, indexing always starts at zero.

full_name = 'Danio rerio'
print(full_name[4])

# Indexing can be performed from the back as well as the front.  The last position is index -1.

full_name = 'Danio rerio'
print(full_name[10])
print(full_name[len(full_name)-1])
print(full_name[-1])

# Slicing allows the capture of part of a string, using the notation start:end.  The first index indicates the start of a slice. The last index indicates the character before which the slice occurs.  The start and end can be left blank.

#slicing list
full_name = 'Danio rerio'
print(full_name[0:3])
print(full_name[3:5])
print(full_name[1:])
print(full_name[:3])

# ### Find

# The find method will return the index of the first character in the search string.  It can take an additional argument indicating where the search will start.  It returns -1 if nothing is found.  There are additional variations of find methods in the `str` module.

#find
full_name = 'Danio rerio'
print(full_name.find('io'))
print(full_name.find('io',5))
print(full_name.find('eo'))
print(full_name.find('1o',10))

dir(str)

# +
# str.rfind?
