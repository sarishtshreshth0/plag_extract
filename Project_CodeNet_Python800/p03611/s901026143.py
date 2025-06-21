import collections

n = int(input())
la = [int(w) for w in input().split()]

cnt = collections.Counter(la)

ans = 0
for c in cnt:
    t = cnt[c-1] + cnt[c] + cnt[c+1]
    ans = max(ans, t)

print(ans)
