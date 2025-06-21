N, K = map(int, input().split())

k_shinsu_list = []
while True:
    k_shinsu_list.append(N % K)
    N = N // K
    if N == 0:
        break
print(len(k_shinsu_list))