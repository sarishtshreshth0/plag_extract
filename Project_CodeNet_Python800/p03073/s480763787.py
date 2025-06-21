S = list(input())
count = 0
for i in range(1,len(S)):
    if(S[i-1]==S[i]):
        if(S[i]=='0'):
            S[i]='1'
            count+=1
        else:
            S[i]='0'
            count+=1
print(count)
