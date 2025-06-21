n = int(input())
l = []
pre_c = None
ans = True
for _ in range(n):
    w = input()
    # print(w)

    if w in l:
        ans = False
        break
    if not(pre_c is None or pre_c == w[0]):
        ans = False
        break

    l.append(w)
    pre_c = w[-1]

if ans:
    print('Yes')
else:
    print('No')