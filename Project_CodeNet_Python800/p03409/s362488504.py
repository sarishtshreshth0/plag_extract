# solution

import io
import sys

data=int(input())

array=[list(map(int,input().split())) for i in range(data) ]

are=[list(map(int,input().split()))  for i in range(data) ]

array.sort(key=lambda x:x[1],reverse=1)

are.sort()

result=0

for b in are:
    for r in array:
        if b[1]>r[1] and b[0]>r[0]:
            result+=1
            array.remove(r)
            break
print(result)