############
#Assigment 7.2
############
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") : 
        ln = line.strip()
        replace = ln.replace("X-DSPAM-Confidence:","")
        total = float(replace)+total
        count = count +1
result = total/count
print ("Average spam confidence:", result)