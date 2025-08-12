# Write a program that first reads in the name of an input file, followed by two strings representing the lower and upper bounds of a search range. 
# The file should be read using the file.readlines() method. The input file contains a list of alphabetical, ten-letter strings, each on a separate line. 
# Your program should output all strings from the list that are within that range (inclusive of the bounds).

file = input().strip()
minVal = input()
maxVal = input()

with open(file) as file:
    for line in file:
        word = line.strip()
        
        if minVal <= word <= maxVal:
            print(word)