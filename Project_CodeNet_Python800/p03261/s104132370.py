a=int(input())
b=[]
for _ in range(a):
    b.append(input())
if len(b)!=len(set(b)):
    print('No')
    exit()
for i in range(a-1):
    if b[i][-1]!=b[i+1][0]:
        print('No')
        exit()
print('Yes')