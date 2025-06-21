def answer(a: int, b: int, c: int, d: int) -> int:
    return max(0, min(b, d) - max(a, c))


def main():
    a, b, c, d = map(int, input().split())
    print(answer(a, b, c, d))


if __name__ == '__main__':
    main()