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

# # Input / Output and File manipulation

# ### User input

# The `input` function will get a string from the user.

# + jupyter={"outputs_hidden": false}
variable = input('Please enter a number: ')
half = float(variable)/2
print('{0} divided by 2 is {1}. Your input was {0}.'.format(variable,half))
# -

# What happens if variable is not changed to float?

# ### Reading and writing files

# The `open` function creates files to read or write. Use 'r' to read, 'w' to write a new file, or 'a' to append to an existing file.

# Writing to a file:

# + jupyter={"outputs_hidden": false}
outfile = open('fishes.txt','w') #'w' indicates write mode
fishes = ['Oryzias latipes','Danio rerio','Takifugu rubripes']

for fish in fishes:
    outfile.write(fish + ' ')

#you need to close the file
outfile.close()
# -

# Reading from a file:

# + jupyter={"outputs_hidden": false}
infile = open('fishes.txt','r')#'r' indicates read mode
text = infile.read()

#you need to close the file
infile.close()

print(text)
# -

# ### Structured Text files

# Files are often saved as tab delimited text or as comma separated values (e.g. from Excel).  The `csv` module allows these to be easily parsed.

# The function `csv.reader` and `csv.writer` also takes the delimiter argument.
# Example: csv.reader(infile,delimiter = '\t')  for tab delimited files.

# Write a file using csv module:

# + jupyter={"outputs_hidden": false}
import csv
outfile = open('fishes.csv','w')
writer = csv.writer(outfile, delimiter = ',') # delimiter indicates what separates items in lists

fishes = ['Oryzias latipes','Danio rerio']
more_fishes = ['Gasterosteus aculeatus','Takifugu rubripes']

writer.writerow(fishes)
writer.writerow(more_fishes)

#you need to close the file
outfile.close()
# -

# Parse CSV files with csv module:

# + jupyter={"outputs_hidden": false}
import csv
infile = open('fishes.csv','r')

reader = csv.reader(infile) 

for line in reader:
    print(line)
    
infile.close()
# -

# ### Importing NumPy arrays

# To import data into arrays use [loadtxt](http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html) or for more complex files [genfromtxt](http://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt).

# + jupyter={"outputs_hidden": false}
import numpy as np
fishes = np.loadtxt('fishes.csv', dtype = str, delimiter=',')  #use skiprows = 1 if you want to skip the header row
print (fishes)
# -

# ### Importing images

# Matplotlib supports image import of .png files using `imread( )`.  For other image types use `scipy.imread( )`.

# + jupyter={"outputs_hidden": false}
# %cd ~/data
# %ls
img = imread('stinkbug.png')
imshow(img)
show()
# -

# ### Getting files from the web

# The [urllib](https://docs.python.org/3/library/urllib.html) module is one of many used for interacting with the web.  One useful function is the `request.urlopen( )` function, which returns an iterable file-like object.

# + jupyter={"outputs_hidden": false}
import urllib

zfin = 'http://zfin.org/downloads/ensembl_1_to_1.txt'

ensembl_markers = urllib.request.urlopen(zfin)
k = 0
for line in ensembl_markers:  
    print(line.strip())                  
    if k>4:
        break
    k += 1

print('--')

# here's an alternate way to do this using enumerate to keep track of iterations

for i,line in enumerate(ensembl_markers):  # enumerate returns index and iterable item
    print(line.strip())                     # strip removes leading and trailing whitespaces (here, gets rid of newline)
    if i>4:
        break
# -

# A more full featured web scraper is found in the [requests](https://requests.readthedocs.io/en/master/) module

# +
import requests

result = requests.get("https://www.oreilly.com/free/")

print(result.status_code)  # http status code; 200, OK; 404, Not Found
# -

# The Python package [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#) parses results by searching for HTML tags

# +
import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.oreilly.com/free/")
c = result.content
soup = BeautifulSoup(c)
samples = soup.find_all("a", "item-title") # finds <a> tag with "item-title"

data = {}
for sample in samples:
    title = sample.string.strip()
    data[title] = sample.attrs['href']
    
print(data['Android Cookbook'])
print(data['Mastering Python'])

# +
import requests
from bs4 import BeautifulSoup

gene_family = 'her'

r = requests.get('https://zfin.org/search', params = {'q':gene_family,'fq':'type:Gene'}) # params passes query data

soup = BeautifulSoup(r.text)
genes = soup.find_all('div', "result-header search-result-name clearfix") # contains search results
print (genes[0])

gene_list = {}
for gene in genes:
    gene_rec = gene.find('a')
    gene_name= gene_rec.string.strip()
    gene_list[gene_name] = gene_rec.attrs['href'][1:]
print(gene_list)
# -

# ### Getting records from NCBI

# The `biopython` package has a lot of useful tools for analyzing sequence data.  In addition it has tools for accessing data from NCBI, including PubMed.

# +
from Bio import Entrez
import json

def search(query):
    Entrez.email = 'your.email@example.com'
    handle = Entrez.esearch(db='pubmed', 
                            sort='relevance', 
                            retmax='20',
                            retmode='xml', 
                            term=query)
    results = Entrez.read(handle)
    return results

def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = 'your.email@example.com'
    handle = Entrez.efetch(db='pubmed',
                            retmode='xml',
                            id=ids)
    results = Entrez.read(handle)
    return results

results = search('zebrafish')
id_list = results['IdList']
papers = fetch_details(id_list)
for i, paper in enumerate(papers['PubmedArticle']): 
    #print (json.dumps(papers, indent=2, separators=(',', ':')))
    print("%d) %s" % (i+1, paper['Authors']['ArticleTitle']['PMID']))
    break
# Pretty print the first paper in full
#import json
#print(json.dumps(papers[0], indent=2, separators=(',', ':')))
# -

# # Interacting with the os

# ### Making directories with the os module

# The `os` module allows manipulation of directories in the operating system.  Here are a few useful functions.

# `os.path.join` generates the appropriate string to make a correct file path.

# + jupyter={"outputs_hidden": false}
import os.path
print(os.path.join('documents','python','exercises'))
# -

# os.path.expanduser( ) generates the correct file path from the user directory.  In Unix, the tilde represents the top level of the file path.

# + jupyter={"outputs_hidden": false}
import os.path
print(os.path.expanduser("~"))

# + jupyter={"outputs_hidden": false}
# os.path.expanduser?
# -

# `os.mkdir( )` will form a new directory.  You will get an error if the directory already exists.

# + jupyter={"outputs_hidden": false}
import os

#first, make a string for the file path
new_folder = os.path.join(os.path.expanduser("~"),'test_mkdir')
print(new_folder)

os.mkdir(new_folder)
#os.mkdir(new_folder)
# -

# `os.chdir( )` will change directory, and `os.listdir( )` will list files in a directory.

# + jupyter={"outputs_hidden": false}
import os
new_folder = os.path.join(os.path.expanduser("~"),'test_mkdir')
os.chdir(new_folder)
os.listdir(new_folder)
# -

# ### Finding file names with glob

# The [glob](http://pymotw.com/2/glob/index.html) function performs a search of Unix file names.  

# + jupyter={"outputs_hidden": false}
#first let's generate a few files.
import os
new_folder = os.path.join(os.path.expanduser("~"),'test_mkdir')
os.chdir(new_folder)

for i in range (4):
    outfile = open('fishes'+str(i)+'.txt','w')
    outfile.close()
    
for i in range (4):
    outfile = open('fish'+str(i)+'.txt','w')
    outfile.close()
    
print(os.listdir(new_folder))
# -

# `glob` returns a list of filenames matching the search string.  It uses * for an undefined length wildcard and ? for single character wildcard.

# + jupyter={"outputs_hidden": false}
import glob

fish = glob.glob('fish*.txt')

print(fish)
# -

# A list of file names becomes an iterable object

# + jupyter={"outputs_hidden": false}
for name in fish:
    print(name)
# -

# You can also match a specific character range in the wildcard.

# + jupyter={"outputs_hidden": false}
fish = glob.glob('fish[13].txt')

print(fish)

# + jupyter={"outputs_hidden": false}
fish = glob.glob('fish[1-3].txt')

print(fish)

# + jupyter={"outputs_hidden": false}
fish = glob.glob('*[1-3].*')

print(fish)
# -

# ### Copying files using Python shutil

# The function `shutil.copy2( )` copies a file along with its metadata and permissions.  It takes the arguments source and destination.  Source indicates the file name, and destination the directory where the copy should be placed.

# + jupyter={"outputs_hidden": false}
import os
import shutil

old_folder = os.path.join(os.path.expanduser("~"),'test_mkdir')
new_folder = os.path.join(os.path.expanduser("~"),'test_mvdir')
os.mkdir(new_folder)

copied_file = 'fish0.txt'
shutil.copy2(os.path.join(old_folder,copied_file),new_folder)
# -

# The function `shutil.copytree( )` copys a directory.  It takes the arguments source and destination.  Source indicates the directory name, and destination the new directory.

# +
import os
import shutil

old_folder = os.path.join(os.path.expanduser("~"),'test_mkdir')
new_folder = os.path.join(os.path.expanduser("~"),'test_mvdir')

shutil.copytree(old_folder,new_folder)
# -

# The function `shutil.move( )` moves a file to a new directory.  It takes the arguments source and destination.  Source indicates the file name, and destination the directory where the file should be placed.

# + jupyter={"outputs_hidden": false}
import os
import shutil

old_folder = os.path.join(os.path.expanduser("~"),'test_mkdir')
new_folder = os.path.join(os.path.expanduser("~"),'test_copydir')

files = os.listdir(old_folder)

for item in files:
    shutil.move(os.path.join(old_folder,item),new_folder)
    
# -


