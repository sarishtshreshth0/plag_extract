N = int(input())
R = [list(map(int, input().split())) for n in range(N)]
B = [list(map(int, input().split())) for n in range(N)]

RY = sorted(R, key=lambda x: x[1], reverse=True)
BX = sorted(B, key=lambda x: x[0])

ans = 0

for b in BX:
  for index, r in enumerate(RY):
    if b[0] > r[0] and b[1] > r[1]:
      ans += 1
      RY.pop(index)
      break

print(ans)