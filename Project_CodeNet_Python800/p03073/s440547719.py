# coding: utf-8
S=list(input())
Acnt=0
Bcnt=0
AList=[]
BList=[]
for i in range(len(S)):
    if i%2==0:
        AList.append(0)
    else:
        AList.append(1)

for j in range(len(S)):
    if j%2==0:
        BList.append(1)
    else:
        BList.append(0)
    
#print(AList)
#print(BList)
    
for k in range(len(S)):
    if int(S[k])!=AList[k]:
        Acnt+=1
    if int(S[k])!=BList[k]:
        Bcnt+=1
        
print(min(Acnt,Bcnt))
