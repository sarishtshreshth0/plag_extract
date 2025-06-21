N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
CD = [list(map(int, input().split())) for _ in range(N)]

def sortx(xy):
  return xy[0]
def sorty(xy):
  return -xy[1]

AB.sort(key=sorty)
CD.sort(key=sortx)

count = 0

for cd in CD:
  for ab in AB:
    if ab[0] < cd[0] and ab[1] < cd[1]:
      count += 1
      AB.remove(ab)
      break

print(count)