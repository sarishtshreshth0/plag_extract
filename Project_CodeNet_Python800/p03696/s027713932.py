N = int(input())
S = list(input())

c = [0,0]
for s in S:
    if s == '(':
        c[0] += 1
    else:
        if c[0] > 0:
            c[0] -= 1
        else:
            c[1] += 1

pre = ['('] * c[1]
rear = [')'] * c[0]
ans = pre+S+rear
print(''.join(ans))
