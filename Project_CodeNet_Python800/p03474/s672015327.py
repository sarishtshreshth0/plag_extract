A,B = map(int, input().split())
S = list(input())
S_h = S.pop(A)

NUM = [str(i) for i in range(10)]
isCorrect = True

if S_h != '-':
    isCorrect = False

for i in S:
    flag = 0
    for j in NUM:
        if i==j:
            flag = 1
    if flag == 0:
        isCorrect = False

if isCorrect:
    print('Yes')
else:
    print('No')
