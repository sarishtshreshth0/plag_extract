n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
t = [list(map(int, input().split()))+[1] for _ in range(n)]

ss = sorted(s, key=lambda x:x[1], reverse=True)
tt = sorted(t, key=lambda x:x[0])
cnt = 0

for i in range(n):
  for j in range(n):
    if ss[i][0] < tt[j][0] and ss[i][1] < tt[j][1] and tt[j][2] == 1:
      cnt += 1
      tt[j][2] -= 1
      break
    
print(cnt)