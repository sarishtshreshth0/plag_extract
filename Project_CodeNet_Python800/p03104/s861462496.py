A, B = map(int, input().split())

def calc(a):
    if a < 0:
        return 0
    ans = 0
    for i in range(50):
        loop = 2 ** (i+1)
        cnt = (a // loop) * (loop // 2)
        cnt += max(0, a % loop+1 - loop // 2)
        if cnt % 2 == 1:
            ans += 2 ** i
    return ans

print(calc(B) ^ calc(A-1))