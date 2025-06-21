a, b, c = map(int, input().split())
l = [i for i in range(min(a, b), max(a, b) + 1)]
if c in l:
    print('Yes')
else:
    print('No')
