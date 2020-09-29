############
#Assigment 7.1
############
fhandle = open("words.txt", "r")
for line in fhandle:
	ln = line.strip()
	print (ln.upper())