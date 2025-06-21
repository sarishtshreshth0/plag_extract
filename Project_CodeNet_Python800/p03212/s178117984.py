import itertools
import bisect
n = int(input())
numbers = []
for i in range(3,10):
    for v in itertools.product(["7","5","3"], repeat=i):
        if "5" in v and "7" in v and "3" in v:numbers.append(int("".join(v)))
numbers.sort()
print(bisect.bisect_right(numbers,n))