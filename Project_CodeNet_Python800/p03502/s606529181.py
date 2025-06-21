X = int(input())
strX = str(X)
fX = 0
for i in range(len(strX)):
    fX += int(strX[i])
if X % fX == 0:
    print('Yes')
else:
    print('No')