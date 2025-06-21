N = int(input())
W = list(map(lambda w: int(w), input().split(" ")))

ary = []
a = 0
s = sum(W)

for i in range(N):
  a += W[i]
  ary.append(abs(s - 2 * a))

print(min(ary))