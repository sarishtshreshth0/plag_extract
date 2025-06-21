def main():
    a, b = map(int, input().split())
    c = [[(b - a) // 2 % 2 ^ b, (b - a + 1) // 2 % 2], [a ^ b ^ (b - a - 1) // 2 % 2, (b - a + 1) // 2 % 2 ^ a]]
    i, j = a % 2, b % 2
    print(c[i][j])


if __name__ == '__main__':
    main()
