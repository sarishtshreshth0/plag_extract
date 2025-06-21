from collections import Counter

N = int(input())
N_list = list(str(N))
number = ['3', '5', '7']
count = 0

def iter_p_adic(p, n):
    from itertools import product
    tmp = [range(p)] * n
    return product(*tmp)

for i in range(len(N_list)):
    iterator = iter_p_adic(3, i+1)
    for idxs in iterator:
        num = []
        for j in range(i+1):
            num.append(number[idxs[j]])
        n = int(''.join(num))
        if len(list(Counter(num))) == 3 and n <= N:
            count += 1

print(count)