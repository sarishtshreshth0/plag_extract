a,n = map(int,input().split())
ans = 0

while a != 0:
  a = a//n
  ans += 1
  
print(ans)