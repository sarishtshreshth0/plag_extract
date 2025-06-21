def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    if N >= M:
        print(0)
        return
    X.sort()
    distance = []
    for i in range(M-1):
        distance.append(X[i+1] - X[i])
    distance.sort()
    for _ in range(N-1):
        distance.pop()
    ans = sum(distance)
    print(ans)

if __name__ == "__main__":
    main()
