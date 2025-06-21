N = int(input())
F = 0
ans = 10 ** 10
i = 1
while i * i <= N:
  A = i
  if N % A == 0:
    B = N // A
    F = max(len(str(A)), len(str(B)))
    ans = min(ans, F)
  i += 1 
print(ans)