import fractions
a = 2
b = int(input())
f = fractions.gcd(a,b)
f2 = a*b//f
print(f2)