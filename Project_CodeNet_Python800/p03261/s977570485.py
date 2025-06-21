n = int(input())
w = [input() for _ in range(n)]

flag=True
if len(set(w))!=n:
    flag=False
    
for i in range(n-1):
    if w[i][-1]!=w[i+1][0]:
        flag=False

print("Yes" if flag else "No")