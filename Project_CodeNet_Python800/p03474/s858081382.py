import sys
sys.setrecursionlimit(4100000)
import math
INF = 10**9

def main():
    a,b = map(int, input().split())
    S = input()

    for i in range(a+b+1):
        if i == a:
            if S[a]!='-':
                print('No')
                return
        else:
            if S[i]=='-':
                print('No')
                return
    print('Yes')


if __name__ == '__main__':
    main()
