N = int(input())
W = list(map(int, input().split()))

all_W = sum(W)
i = 0
s1 = 0
while i < N:
  s1 = s1 + W[i]
  s1_minus_s2 = all_W - 2 * s1
  if s1_minus_s2 <= 0:
    print(min(abs(s1_minus_s2), abs(s1_minus_s2 + 2 * W[i])))
    break
  i += 1