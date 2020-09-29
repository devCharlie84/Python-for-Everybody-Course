############
# Assigment 4.6
############
def computepay(h, r):
    if(h < 40):
        payment = r*h
        return payment
    else:
        resta = h-40
        payment = (r*resta)*1.5
        payment = payment + r*40
        return payment


hrs = input("Enter Hours:")
rate = input("Rate per hour:")

hrs_f = float(hrs)
rate_f = float(rate)

p = computepay(hrs_f, rate_f)
print("Pay", p)