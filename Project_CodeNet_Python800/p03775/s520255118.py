import math

N = int(input())

d=[]

for i in range(1,int(math.sqrt(N))+1):
    if N%i == 0:
        d.append(N//i)
        d.append(i)
    
Fmin=10**10

for i in d:
    if N%i ==0:
        A = i
        B = N//i
        F = max(len(str(A)),len(str(B)))
        if F < Fmin:
            Fmin = F
print(Fmin)
