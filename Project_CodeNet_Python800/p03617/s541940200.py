import sys
def input():
    return sys.stdin.readline()[:-1]
def main():
    Q, H, S, D = map(int,input().split())
    N = int(input())
    print((N//2)*min(Q*8,H*4,S*2,D)+(N%2)*min(Q*4,H*2,S))
    
if __name__ == '__main__':
    main()
