import sys

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())


def main():
    N, M = mi()
    X = list(mi())
    X.sort()
    if N >= M:
        print(0)
        return
    dif = [(X[i+1]-X[i], i) for i in range(M-1)]
    dif.sort(reverse=True)
    koma = [-1]+[dif[i][1] for i in range(N-1)]+[M-1]
    print(sum(X[koma[i+1]]-X[koma[i]+1] for i in range(N)))

if __name__ == '__main__':
    main()
