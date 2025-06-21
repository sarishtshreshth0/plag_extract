import collections
N = input()
a = list(map(int,input().split()))

a_count = collections.Counter(a)

total = 0
for i in a_count.keys():
    total = max(total,a_count[i-1] + a_count[i] + a_count[i+1])
print(total)