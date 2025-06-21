n , a, b = map(int, input().split())
s = input()
t = 0
count = 1
ans = []
for i in range(n):
    if s[i] == 'a' and count <= (a+b):
        ans.append('Yes')
        count += 1
    elif s[i] == 'b':
        t += 1
        if count <= (a+b) and  t <= b:
            ans.append('Yes')
            count += 1
        else:
            ans.append('No')
    else:
        ans.append('No')
for i in ans:
    print(i)