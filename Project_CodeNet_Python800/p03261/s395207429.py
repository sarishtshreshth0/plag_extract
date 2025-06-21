n=int(input())
w=[]
f=0
for i in range(n):
    w.append(input())
for i in range(n-1):
    if w[i][len(w[i])-1]==w[i+1][0]:
        f+=1
for i in range(n):
    if w.count(w[i])==1:
        
        f+=1
print("Yes" if f==2*n-1 else "No")
            
