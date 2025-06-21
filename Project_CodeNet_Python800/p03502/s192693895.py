N = int(input())


def sum_of_num(num):
    list_a = []
    sums = 0
    while num > 0 :
        list_a.append(num % 10)
        num = num //10
    for i in range(len(list_a)):
        sums = sums + list_a[i]
    return sums

fx = sum_of_num(N)

if N % fx == 0:
    print('Yes')
if N % fx != 0:
    print('No')