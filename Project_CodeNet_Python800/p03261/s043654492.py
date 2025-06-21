n = int(input())
seen = set()
for i in range(n):
    s = input()
    if i > 0 and s[0] != pre or s in seen:
        print('No')
        break
    seen.add(s)
    pre = s[-1]
else:
    print('Yes')
