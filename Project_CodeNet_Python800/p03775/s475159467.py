import sys
import math
input = lambda: sys.stdin.readline()
exec("try:sys.stdin=open('input.txt','r');sys.stdout=open('output.txt','w')\nexcept:pass")

length = lambda x: len(str(int(x)))

n = int(input())
ans = []
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        if n // i == i:
            ans.append(length(n // i))
        else:
            ans.append(max(length(i), length(n // i)))
print(min(ans))
