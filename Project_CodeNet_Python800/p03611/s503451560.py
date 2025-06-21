from collections import defaultdict


def main():
    N = int(input())
    a = list(map(int, input().split()))

    d = defaultdict(int)
    for aa in a:
        for i in range(-1, 2):
            d[aa+i] += 1

    ans = 0
    for k in d:
        if d[k] > ans:
            ans = d[k]

    print(ans)


if __name__ == "__main__":
    main()
