n,a,b = map(int,input().split())
s=[]
s_in = input()
for i in range(n):
    s.append(s_in[i])
pass_all = 0
pass_kaigai = 0
judge=[]
for i in range(n):
    if s[i] == "a":
        if pass_all < a + b:
            judge.append("Yes")
            pass_all += 1
        else:
            judge.append("No")
    elif s[i] == "b":
        if pass_all < a+b and pass_kaigai < b:
            judge.append("Yes")
            pass_all += 1
            pass_kaigai += 1
        else:
            judge.append("No")
    else:
        judge.append("No")
for i in range(n):
    print(judge[i])
