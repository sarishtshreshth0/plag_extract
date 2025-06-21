N = int(input())
S = input().rstrip()
res = 1
s0 = S[0]
for s in S[1:]:
    if s != s0:
        res += 1
    s0 = s
print(res)