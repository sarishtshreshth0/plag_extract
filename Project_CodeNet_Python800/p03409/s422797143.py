n = int(input())

red = [0]*n
for i in range(n):
  a, b = map(int, input().split())
  red[i] = (a, b)
red.sort()

blue = [0]*n
for i in range(n):
  c, d = map(int, input().split())
  blue[i] = (c, d)
blue.sort()

ans = 0
pair_judge = [False]*(2*n+1)
k = 0
for i in range(n):
  a, b = blue[i][0], blue[i][1]
  while True:
    if k < n and red[k][0] < a:
      pair_judge[red[k][1]] = True
      k += 1
      continue
    else:
      break
  for j in range(b-1, -1, -1):
    if pair_judge[j]:
      ans += 1
      pair_judge[j] = False
      break

print(ans)