n = int(input())
s = input()

slime = []
slime.append(s[0])
for i in range(1, n):
    if s[i-1] == s[i]:
        continue
    else:
        slime.append(s[i])

print(len(slime))
