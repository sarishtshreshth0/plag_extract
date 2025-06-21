import math as m
n=int(input())
A=1
B=n
for i in range(1, int(m.sqrt(n))+1):
    if n % i == 0:
        A, B = i, n // i

print(int(m.log10(B))+1)
