import sys
import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
from collections import deque
from bisect import bisect_left
from itertools import product
def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LI2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
#文字列を一文字ずつ数字に変換、'5678'を[5,6,7,8]とできる
def LSI(): return list(map(int, list(sys.stdin.readline().rstrip())))
def LSI2(N): return [list(map(int, list(sys.stdin.readline().rstrip()))) for i in range(N)]
#文字列として取得
def ST(): return sys.stdin.readline().rstrip()
def LST(): return sys.stdin.readline().rstrip().split()
def LST2(N): return [sys.stdin.readline().rstrip().split() for i in range(N)]
def FILL(i,h): return [i for j in range(h)]
def FILL2(i,h,w): return [FILL(i,w) for j in range(h)]
def FILL3(i,h,w,d): return [FILL2(i,w,d) for j in range(h)]
def FILL4(i,h,w,d,d2): return [FILL3(i,w,d,d2) for j in range(h)]
def sisha(num,digit): return Decimal(str(num)).quantize(Decimal(digit),rounding=ROUND_HALF_UP)
#'0.01'や'1E1'などで指定、整数に戻すならintをかます
MOD = 1000000007
INF = float("inf")
sys.setrecursionlimit(10**6+10)

S = list(ST())
T = list(ST())
dp = FILL2(0,len(S)+1,len(T)+1)
for i in range(len(S)+1):
    for j in range(len(T)+1):
        if i+1<=len(S) and j+1<=len(T):
            if S[i]==T[j]:
                dp[i+1][j+1] = dp[i][j] + 1
        if i+1<=len(S):
            dp[i+1][j] = max(dp[i+1][j],dp[i][j])
        if j+1 <= len(T):
            dp[i][j+1] = max(dp[i][j+1],dp[i][j])

l = dp[len(S)][len(T)]
i = len(S)
j = len(T)
ans = ''
while l > 0:
    if S[i-1]==T[j-1]:
        i -= 1
        j -= 1
        l -= 1
        ans = S[i]+ans
    else:
        if dp[i][j-1]==dp[i][j]:
            j -= 1
        else:
            i -= 1
print(ans)
