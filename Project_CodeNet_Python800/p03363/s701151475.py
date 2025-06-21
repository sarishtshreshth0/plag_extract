n = int(input())
l = list(map(int, input().split()))

def cumulative_sum(collection):
    result = [0]
    for item in collection:
        result.append(result[-1] + item)
    return result
cm = cumulative_sum(l)

def combination(items_num, pair_num):
    if items_num < pair_num: return 0
    if items_num - pair_num < pair_num: pair_num = items_num - pair_num
    if pair_num == 0: return 1
    if pair_num == 1: return items_num
    numerator   = [items_num - pair_num + k + 1 for k in range(pair_num)]
    denominator = [k + 1 for k in range(pair_num)]
    for p in range(2, pair_num+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (items_num - pair_num) % p
            for k in range(p-1, pair_num, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot
    result = 1
    for k in range(pair_num):
        if numerator[k] > 1:
            result *= int(numerator[k])
    return result

from collections import Counter
c = Counter(cm)
ans = 0
from scipy.special import comb
for i in c.keys():
        ans += int(comb(c[i], 2))

print(ans , flush=True)
