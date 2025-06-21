n,a,b = map(int,input().split())
s = input()
x = a + b
y = 1
z = 1
for i in range(n):
    if s[i] == 'a':
        if y <= x:
            print('Yes')
            y += 1
        else:
            print('No')
    elif s[i] == 'b':
        if y <= x and z <= b:
            print('Yes')
            y += 1
            z += 1
        else:
            print('No')
    else:
        print('No')