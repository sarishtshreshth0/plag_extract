S = input().rstrip()
w = 0
b = 0
for i in range(len(S)):
    if i%2==0 and int(S[i])==0:
        w += 1
    elif  i%2==1 and int(S[i])==1:
        w += 1
    elif  i%2==0 and int(S[i])==1:
        b += 1
    elif  i%2==1 and int(S[i])==0:
        b += 1
print(min(w,b))