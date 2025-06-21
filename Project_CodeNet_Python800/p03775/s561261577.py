from math import sqrt
N = int(input())

ans = 100
sq_n = int(sqrt(N))
for i in range(1, sq_n+1):
  if N % i == 0:
    ans = min(ans, max(len(str(i)),len(str(N//i))))
print(ans)