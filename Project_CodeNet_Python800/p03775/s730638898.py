import math
n = int(input())
for i in range(int(n**0.5),0,-1):
    if n%i == 0:
        a = max(i,n//i)
        print(int(math.log10(a))+1)
        break