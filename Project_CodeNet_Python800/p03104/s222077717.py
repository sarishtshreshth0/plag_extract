from math import ceil


def main():
    a, b = map(int, input().split())
    answer = 0
    if a < b:
        for i in range(a, ceil(a / 4) * 4):
            answer ^= i
        for i in range((b // 4) * 4, b + 1):
            answer ^= i
    else:
        answer = a
    print(answer)


if __name__ == '__main__':
    main()

