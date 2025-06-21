Q, H, S, D = map(int, input().split())
N = int(input())

c_05 = min(2*Q, H)
c_1 = min(2*c_05, S)

if 2*c_1 <= D:
    print(c_1 * N)
else:
    if N % 2 == 0:
        print(D * (N//2))
    else:
        print(D * (N//2) + c_1)