n, a, b = map(int,input().split())
s = input()


tuka = 0
kaigai = 0
for i in range(1,n+1):
    if s[i-1] == 'a':
        if tuka < a+b:
            print('Yes')
            tuka += 1
        else:
            print('No')
    elif s[i-1] == 'b':
        if tuka < a+b and kaigai < b:
            print('Yes')
            tuka += 1
            kaigai += 1
        else:
            print('No')
    else:
        print('No')
