############
# Assigment 3.1
############
hrs = input("Enter Hours:")
rate = input("Enter rate per hour:")

try:
    r = float(rate)
    h = float(hrs)
except:
    print("Error, please insert the request values")

if(h < 40):
    pay = r*h
    print(pay)

else:
    resta = h-40
    pay = (r*resta)*1.5
    pay = pay + r*40
    print(pay)
