S=input()
if len(S)%2==0:
    black="01"*(len(S)//2)
    white="10"*(len(S)//2)
    countb=0
    countw=0
else:
    black="01"*(len(S)//2)+"0"
    white="10"*(len(S)//2)+"1"
countb=0
countw=0
for i in range(len(S)):
    if S[i]!=black[i]:
        countb=countb+1
    elif S[i]!=white[i]:
        countw=countw+1
    else:
        pass
if countb>=countw:
    print(countw)
else:
    print(countb)