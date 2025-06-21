import math
n=int(input())

s=1
for i in range(int(math.sqrt(n))+1):
    if n%(i+1)==0:
        s=len(str(int(n/(i+1))))
print(s)