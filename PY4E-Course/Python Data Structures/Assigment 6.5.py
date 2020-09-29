############
#Assigment 6.5
############
text = "X-DSPAM-Confidence:    0.8475";
lenght = len(text)
numberstr = text.find('0')
number = text[numberstr:lenght+1]
print (float(number))