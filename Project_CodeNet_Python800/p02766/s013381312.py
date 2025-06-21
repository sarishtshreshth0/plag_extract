#ABC156B
n,k = map(int,input().split())
ans = 0
while n > 0 :
    n = n // k
    ans = ans + 1
print(ans)