
n=int(input())
r=[[0]*3 for i in range(n)]
b=[[0]*2 for i in range(n)]
for i in range(n):
    r[i]=list(map(int,input().split()))+[0]
for i in range(n):
    b[i]=list(map(int,input().split()))

r.sort(key=lambda x:x[1],reverse=True)
b.sort()

psum=0
for i in range(n):
    for ii in range(n):
#        print("b:",i,b[i][0],b[i][1],"r:",ii,r[ii][0],r[ii][1])
        if b[i][0]>r[ii][0] and b[i][1]>r[ii][1] and r[ii][2]==0:
            r[ii][2]=1
            psum+=1
            break
print(psum)
            
