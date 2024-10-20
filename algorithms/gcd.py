#Finding Greatest Common Denominator of two numbers
#Using Euclid's algorithm

def gcd(a,b):
    while (b != 0):
        t = a
        a = b
        b = t % a
    return a
print(gcd(8,20))