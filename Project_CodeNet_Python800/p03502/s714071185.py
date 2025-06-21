s = input()
n = int(s)
cnt = 0
for a in s:
    cnt += int(a)
if n % cnt == 0:
    print("Yes")
else:
    print("No")