n = int(input())

lis = []
for _ in range(n):
    lis.append(input())
    
if len(lis) != len(set(lis)):
    print("No")
    exit()
 
tmp = lis[0][-1]
for i in range(1,n):
    if lis[i][:1] != tmp:
        print("No")
        exit()
    else:
        tmp = lis[i][-1]

print("Yes")