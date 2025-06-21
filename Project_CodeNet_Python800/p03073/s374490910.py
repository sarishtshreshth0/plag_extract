A=input()
S=[]
for i in A:
    S.append(int(i))

ans_1=0
ans_2=0
for i in range(1,len(S)+1):
    if i%2!=0:
        if S[i-1]!=0:
            ans_1+=1
    else:
        if S[i-1]==0:
            ans_1+=1
        

for i in range(1,len(S)+1):
    if i%2!=0:
        if S[i-1]!=1:
            ans_2+=1
    else:
        if S[i-1]==1:
            ans_2+=1

print(min(ans_1,ans_2))