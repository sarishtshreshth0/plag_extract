import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

X = int(input())
big_coin, amari = divmod(X, 500)
print(big_coin*1000+(amari//5)*5)