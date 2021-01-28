# This was developed for an assignment that invloves opening a text file, and creating
# a list of "new" words to add to that list.  Below are the assignment instructions.
# I have included romeo.txt with this repository as it was the file we had to search
# through. 

# 8.4 Open the file romeo.txt and read it line by line. For each line, split the
# line into a list of words using the split() method. The program should build a
# list of words. For each word on each line check to see if the word is already in
# the list and if not append it to the list. When the program completes, sort and
# print the resulting words in alphabetical order.

fname = input("Enter file name: ")
fh = open(fname)
lst = []
grp = []
for line in fh:
    lst = line.split()
    for word in lst:
        grp.append(word)
fgrp = list(set(grp))
fgrp.sort()
print(fgrp)
