# II - Automating Tasks
# 08 - Read and Write Files
# Book Examples from Chapter

import os

# Function to print the header of each section nicely formatted
def printHeader(header):
    print("******************************************************************************\n")
    header = "*** " + header.upper() + " ***"
    print(header)


# Get current working directory, and join text into an OC agnostic directory string
printHeader("Get current working directory, and join text into an OS agnostic directory string")
print(os.getcwd())
print(os.path.join('usr', 'bin', 'spam'))   # works with any operating system

# Creating New Folders with os.makedirs()
printHeader("Creating New Folders with os.makedirs()")
folderString = 'C:\\ZZ-DELETE\deleteThisToo\AlsoDeleteThis'
# print("-- Creating folder at: " + folderString)   # Uncomment this with the line below
# os.makedirs(folderString)                         # Uncomment this to create the folders (I commented it out since it was creating them over and over)

# The os.path Module
printHeader("The os.path Module")
# os.path has many helpful functions related to filenames and file paths
# Whenever your programs need to work with files, folders, or file paths, you can refer to the short examples in this section. 
# The full documentation for the os.path module is on the Python website at http://docs.python.org/3/library/os.path.html

# Handling Absolute and Relative Paths
printHeader("Handling Absolute and Relative Paths")
print(os.path.abspath('.') )    # d:\Dropbox\Programming\Courses\Python, DS\Automate with Python\08-Read Write Files
print(os.path.abspath('.\\PreMadeFolder') ) # d:\Dropbox\Programming\Courses\Python, DS\Automate with Python\08-Read Write Files\PreMadeFolder
print(os.path.isabs('.') )  # False
print(os.path.isabs(os.path.abspath('.')) ) # True
print(os.path.relpath('C:\\Windows', 'C:\\') ) # Windows

# Directory (dir) name vs base name
printHeader("Directory (dir) name vs base name")
calcPath = "C:\Windows\System32\calc.exe"
print(os.path.basename(calcPath) ) # basename = filename = "calc.exe"
print(os.path.dirname(calcPath) ) # dirname = directory name = "C:\Windows\System32"
print(os.path.split(calcPath) ) # split has both the dirname and basename together as a tuple
print(os.path.dirname(calcPath),  os.path.basename(calcPath) )
print(os.path.split(os.path.sep) )

# Finding File Sizes and Folder Contents
printHeader("Finding File Sizes and Folder Contents")
print(os.path.getsize(calcPath) )
calcDirPath = os.path.dirname(calcPath)
print(os.listdir(calcDirPath)[:20] )    # print the first 20 folders in C:\Windows\System32
print("Get the total size of all the files in the Windows System32 Directory:")
totalSize = 0
for filename in os.listdir(calcDirPath):
    totalSize = totalSize + os.path.getsize(os.path.join(calcDirPath, filename))
print(totalSize)

# Checking Path Validity
printHeader("Checking Path Validity")
print(os.path.exists('C:\\Windows') )                           # True
print(os.path.exists('C:\\some_made_up_folder') )               # False
print(os.path.isdir('C:\\Windows\\System32') )                  # True
print(os.path.isfile('C:\\Windows\\System32') )                 # False
print(os.path.isdir('C:\\Windows\\System32\\calc.exe') )        # False
print(os.path.isfile('C:\\Windows\\System32\\calc.exe') )       # True
# check if the Multimedia NASKICKER is connected and logged in with pw
print(os.path.exists('M:\\'))                                   # True (should be)

# The File Reading / Writing Process
printHeader("The File Reading / Writing Process")
print(os.getcwd() )
print(os.listdir(os.getcwd()))
helloFile = open('hello.txt')
helloContent = helloFile.read()
print(helloContent)
sonnetFile = open('sonnet29.txt')
print(sonnetFile.readlines())

# Writing to Files
printHeader("Writing to Files")
baconFile = open('bacon.txt', 'w')  # w = write mode.  Will overwrite things that are already there
baconFile.write('Hello world!\n')
baconFile.close()
baconFile = open('bacon.txt', 'a')    # a = append mode.  Will leave what is already there and add to the end
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

# Saving Variables with the shelve Module
printHeader("Saving Variables with the shelve Module")
import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
shelfFile = shelve.open('mydata')
type(shelfFile)
shelfFile['cats']
shelfFile.close()
shelfFile = shelve.open('mydata')
list(shelfFile.keys() )             # shelf values are stored like dictionaries with keys and values
list(shelfFile.values() )
shelfFile.close()

# Saving Variables with pprint.pformat() Function
printHeader("Saving Variables with pprint.pformat() Function")
import pprint
cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
print(pprint.pformat(cats) )
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()     # note that this is saved as a standard .py python file and can be opened with import
print("... now to test importing the myCats file saved with .write")
import myCats
print(myCats.cats)
print(myCats.cats[0])
print(myCats.cats[0]['name'])