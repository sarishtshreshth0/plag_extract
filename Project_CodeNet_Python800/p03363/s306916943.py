from collections import defaultdict


def main():
    N = int(input())
    A = list(map(int, input().split()))
    counter = defaultdict(int)
    counter[0] = 1
    cumsum = 0
    ans = 0
    for a in A:
        cumsum += a
        ans += counter[cumsum]
        counter[cumsum] += 1
    print(ans)


if __name__ == '__main__':
    main()