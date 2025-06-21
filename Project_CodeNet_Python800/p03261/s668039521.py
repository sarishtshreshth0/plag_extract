n = int(input())
l = str(input())

l = [l]

ans = 0
for i in range(n-1):
    x = str(input())
    if x not in l and l[i][-1]==x[0]:
        l.append(x)
        continue
    else:
        ans = -10000000000
        break
if ans == 0:
    print('Yes')
else:
    print('No')
