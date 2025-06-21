# 最大公約数(mathは3.5以降) 
import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

# 初期入力
import sys
#input = sys.stdin.readline  #文字列では使わない
N,X = map(int, input().split())
x = list(map(int, input().split()))

# ｘの隣同士の距離リスト
x_div =[abs(X-x[0])] #初項
for i in range(N-1):
    x_div.append(abs(x[i] -x[i+1]))

#x_divの最大公約数
if N ==1:
    ans =abs(x[0] -X)
else:
    ans =gcd_list(x_div)
print(ans)