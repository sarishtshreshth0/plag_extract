from sys import stdin
def LI(): return list(map(int,stdin.readline().rstrip().split()))

tmp = LI()
for i in range(2):
    if tmp[i]==1:
        tmp[i] = 999

a,b = [tmp.pop(0) for _ in range(2)]

if a<b:
    print('Bob')
elif b<a:
    print('Alice')
else:
    print('Draw')