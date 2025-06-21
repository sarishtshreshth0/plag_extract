mod = 1000000007
eps = 10**-9


def main():
    import sys
    from collections import deque
    input = sys.stdin.readline

    N = int(input())
    que = deque(["3", "5", "7"])
    ans = 0
    while True:
        i = que.popleft()
        if int(i) > N:
            break
        if "3" in i and "5" in i and "7" in i:
            ans += 1
        que.append(i + "3")
        que.append(i + "5")
        que.append(i + "7")
    print(ans)


if __name__ == '__main__':
    main()
