N = int(input())
S = input()
assert len(S) == N

# 隣接するスライムは同色なら融合し1体に
count = 0
color = ''
for c in S:
  if c != color:
    color = c
    count += 1
print(count)