n = int(input())
str_n = str(n)
wa = 0
for i in range(len(str_n)):
    wa += int(str_n[i])
if n%wa==0:
    print('Yes')
else:
    print('No')