n = int(input())
S = input()
beforeChara = ""
cnt = 0
for s in S:
    if s != beforeChara:
        cnt += 1
    beforeChara = s
print(cnt)