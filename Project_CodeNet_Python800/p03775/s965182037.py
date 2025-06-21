"""
全探索
N<=1e10なのでa<=math.sqrt(N)まで調べればよい
"""
import math
n = int(input())
mn = 1e10
for a in range(1,int(math.sqrt(n))+1) :
    if n%a == 0 :
        b = str(n//a)
        a = str(a)
        mn = min(mn,max(len(a),len(b)))
print(mn)
