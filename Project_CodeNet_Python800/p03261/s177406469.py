N = int(input())
S = [input() for _ in range(N)]
d = dict()
prev = ''
for i, s in enumerate(S):
    if i > 0 and s[0] != prev:
        print('No')
        break
    if d.get(s, 0) > 0:
        print('No')
        break
    d[s] = 1
    prev = s[-1]
else:
    print('Yes')