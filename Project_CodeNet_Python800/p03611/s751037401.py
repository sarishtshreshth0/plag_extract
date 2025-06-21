N = int(input())
A = list(map(int, input().split()))

ans = 0
A = sorted(A)
#print(A)
l = 0
for i in range(1, N):
  while A[i] - A[l] > 2:
    l += 1
  now = i - l + 1
  ans = max(ans, now)
  #print(i, l, ans, now)
  
print(max(ans, 1))



