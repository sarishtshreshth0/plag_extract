n, d = map(int, input().split())
data = [ list(map(int, input().split())) for _ in range(n) ]

def f(list_1, list_2):
    len_ = len(list_1)
    sum_ = 0
    for i in range(len_):
        sum_ += ( list_1[i] - list_2[i] ) ** 2
    return sum_

count = 0
for i in range(n):
    for j in range(i):
        if i == j:
            continue
        # print("j_i", j, i)
        if f(data[i], data[j])**0.5 % 1 == 0.0:
            count += 1

print(count)
