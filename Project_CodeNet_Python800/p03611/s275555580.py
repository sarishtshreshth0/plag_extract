# vim: fileencoding=utf-8


def main():
    n = int(input())
    bucket = [0] * ((10 ** 5) + 1)
    a = list(map(int, input().split()))
    for i in a:
        bucket[i] += 1
        if i > 0:
            bucket[i - 1] += 1
        if i < 10 ** 5:
            bucket[i + 1] += 1
    print(max(bucket))


if __name__ == "__main__":
    main()
