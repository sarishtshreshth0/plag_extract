n, d = list(map(int, input().split()))

x = [list(map(int, input().split())) for _ in range(n)]

def is_square_num(n):
  i2 = 0
  for i in range(0, n + 1):
    if i2 == n:
      return True
    if i2 > n:
      return False
    i2 += i * 2 + 1

c = 0

for i in range(n-1):
    for j in range(i+1, n):
        dist = 0
        for k in range(d):
            dist += (x[i][k] - x[j][k]) ** 2

        if is_square_num(dist):
            c += 1

print(c)