import math

def gcd(a,b):

    #handles negative numbers 
    a =abs(a)
    b =abs(b)
    
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(54, 24))  # Expected output: 6
print(gcd(48, 18))  # Expected output: 6
print(gcd(101, 10))  # Expected output: 1
print(gcd(-200, 24))  # Expected output: 8

