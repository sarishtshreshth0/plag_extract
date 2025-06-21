from itertools import product
N = int(input())

keta = len(str(N))
# print('keta:',keta)

count=0
for i in range(3,keta+1):
    a = ["7","5","3"]
    As = list(product((a), repeat=i))
    for A in As:
        # print('A:',A)
        if ("3" in A) and ("5" in A) and ("7" in A):
            S = int("".join(A))
            if S <=N:
                count+=1

print(count)
