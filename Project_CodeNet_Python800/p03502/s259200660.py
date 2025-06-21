N = int(input())
N_list = list(str(N))
n = 0
for i in N_list:
    n += int(i)

if N % n == 0:
    print('Yes')
else:
    print('No')