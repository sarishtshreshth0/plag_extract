N = input().strip()
a = 0
for i in range(len(N)):
    a += int(N[i])
if int(N)%a==0:
    print("Yes")
else:
    print("No")