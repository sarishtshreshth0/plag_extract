import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    s=str(input())
    print('Yes' if s[:4]=='YAKI' else 'No')
    
resolve()