dic = {}
N = int(input())
pre = input()
dic[pre] = 0
flag = True
for i in range(N-1):
    s = input()
    if list(pre)[len(pre)-1]!=list(s)[0]:
        flag=False

    if s in dic:
        flag=False
    else:
        dic[s]=0

    pre = s

print("Yes" if flag else "No")