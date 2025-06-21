N = int(input())
S = list(input())

ans = []
count = 0
addFlag = True
for i in range(N):
    if addFlag:
        if S[i] == ')':
            ans.append(')')
            ans.insert(0,'(')
        else:
            ans.append('(')
            count += 1
            addFlag = False
    else:
        if S[i] == '(':
            ans.append('(')
            count += 1
        else:
            ans.append(')')
            count -= 1
            if count == 0:
                addFlag = True

for _ in range(count):
    ans.append(')')

print(''.join(ans))