import collections
n,cc = raw_input(),collections.Counter(map(int, raw_input().split()))
print max([cc[k] + cc[k+1] + cc[k-1] for k in cc] or [0])
