import sys
input = sys.stdin.readline
import math
from functools import reduce


# 最大公約数（リスト引数）
def gcd_list(numbers):
    return reduce(math.gcd, numbers)


N, X = [int(a) for a in input().split()]
x = [int(a) for a in input().split()]

# 座標XからDずつ移動してぴったりxkを訪れられる
# ⇄ |X - xk|がDで割り切れる
# ⇄ Dは|X-x1|,|X-x2|,...,|X-xN|の公約数
# つまりDの最大値は、|X-x1|,|X-x2|,...,|X-xN|の最大公約数

nums = [abs(X - xk) for xk in x]
ans = gcd_list(nums)
print(ans)