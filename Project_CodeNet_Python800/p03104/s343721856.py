import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def f(n):
    res = 0
    if n == 0:
        return 0
    else:
        if n % 2 == 0:
            res = n
            n -= 1
        res = res ^ (((n + 1) // 2) % 2)
    return res


def main():
    a, b = input_int_list()
    # f(A,B) = f(0,a-1) XOR f(0,b)
    # n が偶数のとき、n XOR n+1 = 1

    if a == 0:
        print(f(b))
        return
    else:
        print(f(b) ^ f(a - 1))
    return


if __name__ == "__main__":
    main()
