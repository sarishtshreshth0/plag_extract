import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())

from collections import defaultdict
dic = defaultdict(int)
for a in As:
    dic[a] += 1
    dic[a-1] += 1
    dic[a+1] += 1

print(max(dic.values()))