import itertools
from bisect import bisect_right

num_lst = []
for i in range(10):
    for lst in itertools.product(["3", "5", "7"], repeat=i):
        if ("3" not in lst) or ("5" not in lst) or ("7" not in lst):
            continue
        num_lst.append(int("".join(lst)))
num_lst.sort()

n = int(input())
print(bisect_right(num_lst, n))
