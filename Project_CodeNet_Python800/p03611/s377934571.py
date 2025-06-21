from collections import defaultdict


def main():
    n = int(input())
    a = [int(an) for an in input().split()]
    cnt = defaultdict(int)
    for an in a:
        for val in {an - 1, an, an + 1}:
            cnt[val] += 1
    print(max(cnt.values()))


if __name__ == "__main__":
    main()
