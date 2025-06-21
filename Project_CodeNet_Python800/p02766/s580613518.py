N, K = map(int, input().split())


def base(value, n):  # 10 => 2
    result = ''
    tmp = int(value)
    while tmp >= n:
        result = str(tmp % n) + result
        tmp = int(tmp / n)
    result = str(tmp % n) + result
    return result


print(len(str(base(N, K))))