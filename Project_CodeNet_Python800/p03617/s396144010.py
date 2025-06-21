Q, H, S, D = map(int, input().split())
N = int(input())
a = N // 2
b = N % 2

money = a * min(8*Q, 4*H, 2*S, D) \
        + b * min(4*Q, 2*H, S)

print(money)
