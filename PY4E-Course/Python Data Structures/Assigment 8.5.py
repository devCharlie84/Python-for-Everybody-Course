############
#Assigment 8.5
############
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
lst = list()
count = 0
for line in fh:
    if line.startswith('From '):
        count = count +1 
        words = line.strip().split()
        print (words[1]) 
print("There were", count, "lines in the file with From as the first word")