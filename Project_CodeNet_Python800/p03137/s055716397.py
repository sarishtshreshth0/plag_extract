def main():
    N, M = map(int, input().split())
    X = [j for j in map(int, input().split())]
    if N >= M:
        print(0)
        exit()
    X.sort()
    s = max(X)-min(X)
    d = [X[i+1]-X[i] for i in range(M-1)]
    d.sort()
    if N == 1:
        print(s)
    else:
        print(s-sum(d[-N+1:]))


main()
