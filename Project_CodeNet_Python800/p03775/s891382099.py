import math
N = int(input())
q = int(math.sqrt(N))
a = 0
for i in range(1,q+1) :
    if N%i == 0 :
        a = i
print(len(str(int(N/a))))