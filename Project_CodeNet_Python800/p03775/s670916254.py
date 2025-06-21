import math

n = int(input())
i = 1
ans = 100000000000
while i <= math.sqrt(n):
    if n%i == 0:
        a = n//i
        b = i
        temp = max(len(str(a)), len(str(b)))
        ans = min(ans, temp)
    i+=1
print(ans)
        

