import math
n = int(input())
best = math.inf
cmb = None
for i in range(int(math.sqrt(n))):
    i+=1
    if n%i==0:
        if best>n//i-i:
            best=n//i-i
            cmb=i

print(int(math.log10(n//cmb))+1)