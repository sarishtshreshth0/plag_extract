from itertools import product
N = int(input())
cnt = 0
num = ["3","5","7"]
for k in range(3,10):
    for x in product(num,repeat=k):
        if x.count("3")>=1 and x.count("5")>=1 and x.count("7")>=1:
            if int("".join(x))<=N:
                cnt += 1
print(cnt)