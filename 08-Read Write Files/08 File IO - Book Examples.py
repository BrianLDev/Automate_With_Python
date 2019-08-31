# II - Automating Tasks
# 08 - Read and Write Files
# Book Examples from Chapter

# Backslack on Windows and Fwd Slash on OSX and Linux
import os
print(os.path.join('usr', 'bin', 'spam'))   # works with any operating system

# Working Directory with cwd
print(os.getcwd())

# Creating New Folders with os.makedirs()
# os.makedirs('C:\\ZZ-DELETE\deleteThisToo\AlsoDeleteThis')

# The os.path Module
# os.path has many helpful functions related to filenames and file paths
# Whenever your programs need to work with files, folders, or file paths, you can refer to the short examples in this section. 
# The full documentation for the os.path module is on the Python website at http://docs.python.org/3/library/os.path.html

# Handling Absolute and Relative Paths
print(os.path.abspath('.') )
print(os.path.abspath('.\\PreMadeFolder') )
print(os.path.isabs('.') )
print(os.path.isabs(os.path.abspath('.')) )

print(os.path.relpath('C:\\Windows', 'C:\\') )

# Directory (dir) name vs base name
path = "C:\Windows\System32\calc.exe"
print(os.path.basename(path) ) # basename = filename = "calc.exe"
print(os.path.dirname(path) ) # dirname = directory name = "C:\Windows\System32"
print(os.path.split(path) ) # split has both the dirname and basename together as a tuple
print(os.path.split(os.path.sep) )


