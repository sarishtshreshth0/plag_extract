import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N = input()
    fN = 0
    for n in N:
        fN += int(n)
    if int(N)%fN==0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
