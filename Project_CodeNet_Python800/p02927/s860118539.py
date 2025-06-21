a, b = [int(i) for i in input().split()]

res = 0

for i in range(1, a+1):
    for j in range(1, b+1):
        ten, one = (j // 10), j % 10
        if ten >= 2 and one >= 2 and ten * one == i:
            res += 1

print(res)