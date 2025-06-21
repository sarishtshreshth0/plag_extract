n = int(input())
f = True
w = input()
used = set([w])
last = w[-1]
for i in range(n-1):
    w = input()
    if w in used or w[0]!=last:
        f = False
        break
    else:
        used.add(w)
        last = w[-1]
if f:
    print('Yes')
else:
    print('No')