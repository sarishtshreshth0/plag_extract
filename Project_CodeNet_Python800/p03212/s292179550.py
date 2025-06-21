from itertools import product
N = int(input())
count = 0
for i in range(3,10):
    a = product(["3","5","7"],repeat=i)
    for b in a:
        if 1<=int("".join(b))<=N and len(set(b))==3:
            count += 1
print(count)