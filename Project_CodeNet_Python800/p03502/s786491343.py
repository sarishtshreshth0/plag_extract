N_str = input()
N = int(N_str)

a = 0
for i in range(len(N_str)):
    a += int(N_str[i])
if N%a == 0:
    print('Yes')
else:
    print('No')
