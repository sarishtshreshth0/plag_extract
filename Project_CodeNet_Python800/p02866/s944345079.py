import sys
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
#MOD = 10 ** 9 + 7
MOD = 998244353
def main():
    N = int(readline())
    D = list(map(int, readline().split()))
    if D[0]!=0:
        print(0)
        exit()
    node = [0]*(max(D)+1)
    for i in range(N):
        node[D[i]] += 1
    if node[0]>1:
        print(0)
        exit()
    ans = 1
    for i in range(len(node)-1):
        ans *= node[i]**node[i+1]
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()