import sys 

n=int(input())
w=[list(input()) for i in range(n)]
flag=True

for i in range(0,n-1):
    if  w[i+1][0]!=w[i][-1]:
        flag=False
for i in range(0,n-1):
    for j in range(1,n):
        if i==j:
            continue
        if w[i]==w[j]: 
            flag=False
if flag :
    print("Yes")
else : print("No")

