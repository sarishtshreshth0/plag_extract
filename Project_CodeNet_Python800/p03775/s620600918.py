import math
N = int(input())
newN = int(math.sqrt(N))
for i in range(1,newN+1):
    if N%i == 0:
        A = i
        B = int(N/i)
print(len(str(B)))