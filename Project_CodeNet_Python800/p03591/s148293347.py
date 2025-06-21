S = input()

t = 'YAKI'
tmp = 0
for i in range(len(S)):
    if S[i] == t[i]:
        flag = True
        tmp += 1
    else:
        flag = False
        break
        
    if tmp == 4:
        break
  
if tmp == 4 and flag == True:
    print('Yes')
    
else:
    print('No')