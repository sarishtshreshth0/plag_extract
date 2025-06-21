ans = 'Yes'
pr = []
n = int(input())
w = input()
pr.append(w)
e = w[-1]
for i in range(n-1):
    w = input()
    if e != w[0] or w in pr:
        ans = 'No'
    pr.append(w)
    e = w[-1]
print(ans)
