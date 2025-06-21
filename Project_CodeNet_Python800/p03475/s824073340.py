N = int(input())

ans = [0] * N
for i in range(N-1):
  C, S, F = map(int, input().split())
  for j in range(i+1):
    if S >= ans[j]:
      ans[j] = S + C
    else:
      ans[j] = F * (1 + (ans[j]-1)//F) + C

for ansi in ans:
  print(ansi)