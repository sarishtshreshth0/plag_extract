def f(n):
    if n % 2 == 0:
        # 偶数で終わっている時
        return n ^ f(n - 1)
    else:
        # 奇数で終わっている時
        return (n // 2 + 1) % 2

def main():
    a, b = map(int, input().split())
    print(f(a-1) ^ f(b))


if __name__ == '__main__':
    main()