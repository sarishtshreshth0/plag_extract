from collections import Counter

N = int(input())
a = list(map(int, input().split()))
ans = []
for x in a:
    ans += [x-1, x, x+1]
c = Counter(ans)
print(c.most_common()[0][1])
