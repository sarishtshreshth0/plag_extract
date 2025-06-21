N=input()

ans = 0
for i in range(len(N)):
	ans += int(N[i])

print("Yes" if int(N)%ans == 0 else "No")