############
#Assigment 8.4
############
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
outputlst = list()
for line in fh:
    lst = line.strip().split() 
    for word in lst:
        if word not in outputlst  :
            outputlst.append(word)
outputlst.sort()
print (outputlst)