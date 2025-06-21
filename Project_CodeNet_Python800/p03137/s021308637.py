import sys
from operator import itemgetter

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(map(int, input().split()))
def iif(n): return [int(input()) for _ in range(n)]
def lmif(n): return [list(map(int, input().split())) for _ in range(n)]
def ss(): return input().split()

def main():
    mod = 1000000007
    
    N, M = mi()
    if N >= M:
        print(0)
        return

    X = lmi()
    X.sort()

    X_dis = []
    for i in range(len(X) - 1):
        X_dis.append(X[i+1] - X[i])
    X_dis.sort()

    if N == 1:
        print(sum(X_dis))
    else:
        print(sum(X_dis[:-N + 1]))

    return

main()
