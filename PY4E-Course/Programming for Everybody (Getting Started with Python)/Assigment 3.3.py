############
# Assigment 3.3
############
score = input("Enter your score:")

try:
    s = float(score)
except:
    print("Error, please insert the request values")

if(s < 1.0) & (s > 0.0):
    if (s >= 0.9):
        print("A")
    elif (s >= 0.8):
        print("B")
    elif (s >= 0.7):
        print("C")
    elif (s >= 0.6):
        print("D")
    elif (s < 0.6):
        print("F")
else:
    print("Error")