import math
n = int(input())
m = int(math.sqrt(n))
s = list()
for i in range(1,m+1):
    if n % i == 0:
        s.append(n/i)
    else:
        continue
print(len(str(int(min(s)))))