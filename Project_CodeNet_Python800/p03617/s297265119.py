Q, T, S, D = map(int, input().split())
N = int(input())

for_1L = min(4*Q, 2*T, S)
for_2L = min(2*for_1L, D)

print((N//2)*for_2L + (N%2)*for_1L)
