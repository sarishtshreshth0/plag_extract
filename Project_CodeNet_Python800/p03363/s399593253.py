import collections
n = int(input())
a = [int(i) for i in input().split()]
acc = [0]
for i in range(n):
    acc.append(acc[-1] + a[i])
dic = collections.defaultdict(int)
for i in range(n+1):
    dic[acc[i]] += 1
ans = 0
for key in dic.keys():
    ans += ((dic[key] * (dic[key]-1)) / 2)
print(int(ans))
