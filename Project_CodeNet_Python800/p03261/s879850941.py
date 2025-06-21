n = int(input())
tmp = []
isOK = True
for i in range(n):
    s = str(input())
    if len(tmp)!=0:
        if s in tmp:
            #print(s,tmp)
            isOK = False
            break
        if end!=s[0]:
            #print(end,s)
            isOK = False
            break
    end = s[-1]
    tmp.append(s)

if isOK:
    print('Yes')
else:
    print('No')