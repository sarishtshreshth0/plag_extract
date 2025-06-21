n = int(input())
l = []
flag = 0
for i in range(n):
    w = input()
    l.append(w)
for k in range(1,n):
    if  l[k-1][-1] != l[k][0]:
        flag =1
        break

    for j in range(k):
        if l[k] == l[j]:
            flag = 1
            break
        
if(flag == 1):
    print('No')
else:
    print('Yes')