import math

def main():
    N, D = map(int, input().split())
    X = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            v = sum((y - z) ** 2 for y, z in zip(X[i], X[j]))
            dist = round(math.sqrt(v))
            if v == dist ** 2:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
