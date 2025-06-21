A,B = map(int,input().split())
S = input()
num = ['0','1','2','3','4','5','6','7','8','9']
ans = True
if len(S)==(A+B+1):
    for i in range(len(S)):
        if i == A:
            if S[i] == '-':
                pass
            else:
                ans = False
                break
        else:
            if S[i] in num:
                pass
            else:
                ans = False
                break
else:
    ans = False

if ans == True:
    print('Yes')
else:print('No')