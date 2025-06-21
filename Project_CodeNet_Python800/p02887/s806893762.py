N = int(input())
S = input() + '*'
ret = 0
for s1, s2 in zip(S, S[1:]):
    if s1 != s2:
        ret += 1
print(ret)
