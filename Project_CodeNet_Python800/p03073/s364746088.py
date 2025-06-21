S = str(input())

ans = 0
cnt = 0
for i in range(len(S)-1):
  if S[i] == S[i+1]:
    cnt += 1
  else:
    ans += (cnt+1) // 2
    if cnt % 2 == 0:
      cnt = 0
    else:
      cnt = 1
ans += (cnt+1) // 2
print(ans)