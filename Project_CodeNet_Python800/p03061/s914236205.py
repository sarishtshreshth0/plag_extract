N = int(input())
As = list(map(int, input().split()))
all_factor = [0 for _ in range(N)]

#%%
from math import gcd
from_right = [0 for _ in range(N)]
from_left = [0 for _ in range(N)]

from_right[-1] = As[-1]
from_left[0] = As[0]

for i in range(N-1):
    from_left[i+1] = gcd(from_left[i], As[i+1])
for i in list(range(N-1))[::-1]:
    from_right[i] = gcd(from_right[i+1], As[i])

answer = 1
for i in range(N):
    if i == 0:
        temp = from_right[1]
    elif i == N-1:
        temp = from_left[N-2]
    else:
        temp = gcd(from_left[i-1],from_right[i+1])
    
    if temp > answer:
        answer = temp
print(answer)