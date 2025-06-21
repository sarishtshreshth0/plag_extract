Q, H, S, D = list(map(int, input().split()))
N = int(input())

calc = N//2 * min(8*Q, 4*H, 2*S, D) + (N%2) * min(4*Q, 2*H, S)

print(calc)