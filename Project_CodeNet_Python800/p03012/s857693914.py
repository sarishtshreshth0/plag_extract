"""abc129_b"""
N = int(input())
W = list(map(int, input().split()))

W_SUM = sum(W)

W_TOTAL = 0
W_ABS = []
for w in W :
    W_TOTAL += w
    W_ABS.append(abs(W_SUM - W_TOTAL * 2))

    if W_TOTAL > W_SUM/2:
        break

print(min(W_ABS))
