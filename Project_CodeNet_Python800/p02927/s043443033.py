import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    M, D = map(int, readline().split())
    ans = 0
    for m in range(1,M+1):
        for d in range(1,D+1):
            d = str(d)
            if len(d)==1:
                d = '0'+d
            if int(d[0])>=2 and int(d[1])>=2 and int(d[0])*int(d[1])==m:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
