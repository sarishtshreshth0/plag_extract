N = input()

L=len(N)

from itertools import product

check_num=[3,5,7]
check=[]

for l in range(1,L+1):
    for p in product(range(3),repeat=l):
        c=''
        for p_ in p:
            c+=str(check_num[p_])
        if len(set(c))==3 and int(c)<=int(N):
            check.append(int(c))
print(len(check))