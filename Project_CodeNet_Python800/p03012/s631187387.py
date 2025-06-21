n=int(input())
w=list(map(int,input().split()))

a=[]

for i in range(0,n):
    ans=(w[:i])
    a.append(abs(2*sum(ans)-sum(w)))
        
print(min(a))