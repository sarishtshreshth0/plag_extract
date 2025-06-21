N=int(input())
A=list(map(int,input().split()))

A_={}
for _ in range(-1,10**5+10):
    A_[_]=0

for a in A:
    a_b = a-1
    a_a = a+1
    A_[a] +=1
    A_[a_b] +=1
    A_[a_a] +=1    

ans = 0
ans_idx = 0
for k in A_.keys():
    a = A_[k]
    if ans < a:
        ans = a
        ans_idx = k
        
# print(ans_idx,ans)
print(ans)