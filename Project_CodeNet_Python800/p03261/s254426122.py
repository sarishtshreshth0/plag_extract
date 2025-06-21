n = int(input())
rule = []
w = input()
rule.append(w)
now = w[-1]
for i in range(n - 1):
    w = input()
    if w in rule:
        print("No")
        exit()
    elif now != w[0]:
        print("No")
        exit()
    else:
        rule.append(w)
        now = w[-1]
print("Yes")