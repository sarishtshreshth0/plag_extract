import sys
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    train = []
    for _ in range(n - 1):
        c, s, f = map(int, input().split())
        train.append((c, s, f))
    
    for i in range(n):
        if i == n - 1:
            print(0)
            continue
        start = i + 1
        time = train[i][0] + train[i][1]
        while start < n - 1:
            if time < train[start][1]:
                time = train[start][0] + train[start][1]
            elif time % train[start][2] == 0:
                time += train[start][0]
            else:
                time += train[start][2] - (time % train[start][2])
                time += train[start][0]
            start += 1
        print(time)


if __name__ == "__main__":
    main()
