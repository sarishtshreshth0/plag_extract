A,B= map(int, input().split())
str1 = input()
li = list(str1)
flag = True
flag2 = False
for i in range(len(li)):
    if li[i] == '-' and i != A:
        flag = False
    elif  li[i] == '-':
        flag2 = True
if flag and flag2:
    print('Yes')
else:
    print('No')