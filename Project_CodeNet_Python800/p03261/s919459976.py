n =int(input())
W=[]
w=''
for i in range(n):
    s=str(input())
    if i !=0 and w[-1] != s[0]:
        print('No')
        exit()
    else:
        w=s
        W.append(w)
if len(W) != len(list(set(W))):
    print('No')
    exit()
print('Yes')