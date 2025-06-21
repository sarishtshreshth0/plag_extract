list_w = []
flag = 0
N = int(input())
for i in range(N):
    W = input()
    list_w.append(W)
    if i >=1 and list_w[-2][-1] != W[0]:
        flag = 1
if len(set(list_w)) != N or flag == 1:
    print('No')
else:
    print('Yes')
