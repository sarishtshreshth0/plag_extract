n = int(input())
ans = n
while(1):
  if ans%2==0 and ans%n==0:
    break
  ans += n
print(ans)