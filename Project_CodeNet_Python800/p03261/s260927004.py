n = int(input())
w = [input() for i in range(n)]
ans = "Yes"
for i in range(n-1):
    if w[i][-1]!=w[i+1][0]:
        ans = "No"
w.sort()
for i in range(n-1):
    if w[i]==w[i+1]:
        ans = "No"
print(ans)