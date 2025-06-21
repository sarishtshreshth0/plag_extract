n = int(input())
s = input()
writtenC = 0
writtenD = 0
for i in range(n):
    if s[i] == ")" and writtenC == 0:
        writtenD += 1
    elif s[i] == ")":
        writtenC -= 1
    else:
        writtenC += 1
print("(" * writtenD + s + ")"*writtenC)
