N, A, B = map(int, input().split())
S = input()
internal = 0
external = 0
res = []
for s in S:
    if s == 'a':
        internal += 1
        res.append('Yes')
    elif s == 'b':
        if external == B:
            res.append('No')
            continue
        external += 1
        res.append('Yes')
    else:
        res.append('No')
    if internal + external == A + B:
        break
res += ['No' for _ in range(N - len(res))]
print(*res, sep='\n')

