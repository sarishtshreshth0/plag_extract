import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = str(input())
if len(S)<4:
    print('No')
elif S[:4]=='YAKI':
    print("Yes")
else:
    print('No')