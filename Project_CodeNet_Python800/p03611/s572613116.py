n=int(input())
A=list(map(int,input().split()))
ans = [0]*(10**5+3)
for i in range(n):
  a = A[i]
  ans[a] += 1
  ans[a+1] += 1
  ans [a+2] += 1
print(max(ans))