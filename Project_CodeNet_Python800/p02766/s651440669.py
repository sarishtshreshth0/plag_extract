from sys import exit
import math
ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

n,k = mi()

ans = 0
while n > 0:
    n //= k
    ans += 1
print(ans)