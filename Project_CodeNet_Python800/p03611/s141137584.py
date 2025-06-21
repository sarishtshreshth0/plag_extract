from collections import defaultdict


def main():
    _ = input()
    a = [int(an) for an in input().split()]
    cnt = defaultdict(int)
    for an in a:
        cnt[an - 1] += 1
        cnt[an] += 1
        cnt[an + 1] += 1
    print(max(cnt.values()))


if __name__ == "__main__":
    main()
