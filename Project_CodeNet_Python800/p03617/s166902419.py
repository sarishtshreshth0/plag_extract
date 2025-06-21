Q, H, S, D = map(int, input().split())
N = int(input()) * 4
L = [[8*Q, 1, Q], [4*H, 2, H], [2*S, 4, S], [D, 8, D]]
L.sort()
ans = 0
for l in L:
  s, t = N // l[1], N % l[1]
  ans += s * l[2]
  N = t
print(ans)