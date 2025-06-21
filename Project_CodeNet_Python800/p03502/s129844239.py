N = input()
num_list = []
for i in N:
    num_list.append(int(i))
if int(N) % sum(num_list) == 0:
    print('Yes')
else:
    print('No')