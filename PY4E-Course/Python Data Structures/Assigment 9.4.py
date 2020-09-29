############
#Assigment 9.4
############
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
lst = list()
lst_emails = list()
emails = dict()
for line in fh:
    if line.startswith('From '):
        linewords = line.strip().split()
        lst.append(linewords[1])
for word in lst :
    emails[word] = emails.get(word,0)+1
largestValue = None
largestKey = None
for key,value in emails.items():
    if largestValue is None or value > largestValue:
        largestValue = value
        largestKey = key
print (largestKey,largestValue)