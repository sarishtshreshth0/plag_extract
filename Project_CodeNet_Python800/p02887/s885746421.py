n = int(input())
s = input()
fusion =[]
tmp = s[0]
fusion.append(tmp)
for i in s[1:]:
    if i != tmp:
        tmp = i
        fusion.append(i)
print(len(fusion))
