#Read a file and handle errors
import os
#open a file and read its content line by line.
#Handle errors that may occur during file operations, such as FileNotFoundError or IOError.
try:
    with open('sample.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
     print("The file 'sample.txt' was not found.")
except IOError:
     print("Error reading file.")