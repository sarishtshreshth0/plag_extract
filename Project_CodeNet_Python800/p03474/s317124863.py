A,B = map(int,input().split())
S = input()

if S[A] == '-':
    Sr = S[:A]+S[A+1:]
    #print(Sr)
    if Sr.isdecimal() == True:
        print('Yes')
    else:
        print('No')
else:
    print('No')