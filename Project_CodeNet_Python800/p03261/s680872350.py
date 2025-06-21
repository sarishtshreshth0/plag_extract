n=int(input())
w=[]
flag=True
for i in range(n):
    w.append(input())
    
for i in range(n-1):
    if w[i][-1]!=w[i+1][0]:
        #print(i,"out1")
        flag=False

for i in range(n-1):
    for j in range(i+1,n):
        if(w[i]==w[j]):
            #print(i,j,"out2")
            flag=False

if flag==True:
    print("Yes")
else:
    print("No")


