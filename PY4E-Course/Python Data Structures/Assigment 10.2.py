############
#Assigment 10.2
############
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
lst = list()
lst_hours = list()
tmp = list()
hoursdic = dict()
output = dict()
for line in fh:
    if line.startswith('From '):
        linewords = line.strip().split()
        lst.append(linewords[5])
for hour in lst :
	linehours = hour.split(":")
	lst_hours.append(linehours[0])
for hour in lst_hours :
    hoursdic[hour] = hoursdic.get(hour,0)+1
for k,v in sorted(hoursdic.items()):
    print (k,v)