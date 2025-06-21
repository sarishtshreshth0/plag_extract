from collections import Counter
N = int(input())
A = list(map(int, input().split()))

cnt = Counter()
for a in A:
    cnt[a-1] += 1
    cnt[a]   += 1
    cnt[a+1] += 1

print(cnt.most_common(1)[0][1])