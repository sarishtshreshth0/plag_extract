#44
S = input()
cou1,cou2 = 0,0
a,b = "",""
if len(S)%2 ==0:
    for i in range(int(len(S)/2)):
        a+="01"
        b+="10"
else:
    for i in range(int(len(S)/2)+1):
        a+="01"
        b+="10"
        
for i in range(len(S)):
    if S[i] != a[i]:
        cou1 +=1
    if S[i] != b[i]:
        cou2 +=1
if cou1 <= cou2:
    cou = cou1
else:
    cou = cou2
        
print(cou)