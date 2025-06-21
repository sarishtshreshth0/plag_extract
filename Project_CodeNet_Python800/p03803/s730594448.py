import sys
sys.setrecursionlimit(10**9)
INF=10**18
def input():
    return sys.stdin.readline().rstrip()

def main():
    a,b=map(int,input().split())
    if a==1:
        a+=13
    if b==1:
        b+=13
    if a>b:
        print('Alice')
    elif a==b:
        print('Draw')
    else:
        print('Bob')    

if __name__ == '__main__':
    main()
