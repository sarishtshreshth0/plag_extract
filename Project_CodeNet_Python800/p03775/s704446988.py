import math
N = int(input())
q = int(math.sqrt(N))
a = 0
for i in range(1,q+1) :
    if N%i == 0 :
        a = i
        b = int(N/a)
print(len(str(b)))