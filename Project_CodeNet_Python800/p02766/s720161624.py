N, K = list(map(int, input().split()))
num = K
count = 1
while num <= N:
    num *= K
    count += 1
print(count)