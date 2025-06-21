X = int(input())
str_X = str(X)
Fx = 0
for i in str_X:
    Fx += int(i)
if X % Fx == 0:
    print('Yes')
else:
    print('No')