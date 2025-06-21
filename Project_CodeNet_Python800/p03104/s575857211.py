a, b = map(int, input().split())

def cal_xor(n):
    if n % 2 == 0:
        if (n // 2) % 2 == 0:
            return 0 ^ n
        else:
            return 1 ^ n
    else:
        if ((n+1)//2) % 2 == 0:
            return 0
        else:
            return 1

print(cal_xor(b)^cal_xor(a-1))