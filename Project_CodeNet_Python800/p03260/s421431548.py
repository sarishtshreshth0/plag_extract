import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    def main():
        A,B=map(int,input().split())
        for i in range(1,4):
            if (A*B*i)%2==1:
                return 'Yes'
        return 'No'
    print(main())

resolve()