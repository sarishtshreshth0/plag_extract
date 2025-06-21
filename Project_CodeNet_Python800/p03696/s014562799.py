N=int(input())
S=input()
n_left=0
n_right=0
for a in S:
    if a==")":
        if n_left==0:
            n_right+=1
        else:
            n_left-=1
    else:
        n_left+=1
print((n_right*"(")+S+(n_left*")"))
