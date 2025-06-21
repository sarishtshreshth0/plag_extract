import sys
def input(): return sys.stdin.readline().strip()

def resolve():
    s=input()
    if s[:4]=='YAKI':
        print('Yes')
    else:
        print('No')
resolve()