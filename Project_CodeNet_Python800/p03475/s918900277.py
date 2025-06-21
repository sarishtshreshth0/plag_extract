def main():
    n = int(input())
    info = [[int(x) for x in input().split()] for _ in range(n - 1)]
    answer = [0 for _ in range(n)]
    for i in range(n - 2, -1, -1):
        now = info[i][1]
        for j in range(i, n - 1):
            if j > i and now % info[j][2]:
                now += info[j][2] - now % info[j][2]
            now = max(now, info[j][1])
            now += info[j][0]
        answer[i] = now
    print("\n".join(map(str, answer)))


if __name__ == '__main__':
    main()

