import itertools
N = input()
keta = len(N)
s = 0
for i in range(3,keta+1):
    a = itertools.product([3,5,7],repeat=i)
    for j in a:
        if 3 in j and 5 in j and 7 in j:
            if int("".join(map(str,j)))<= int(N):
                s +=1
print(s)