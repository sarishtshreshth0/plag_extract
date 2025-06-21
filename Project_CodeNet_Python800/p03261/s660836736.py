n = int(input())
w = []
for i in range(n):
    w.append(input())
ok = True
for i in range(n-1):
    sz = len(w[i])
    if w[i][sz-1] != w[i+1][0]: ok = False
for i in range(n):
    for j in range(n):
        if i != j and w[i] == w[j]:
            ok = False
if ok: print('Yes')
else: print('No')
