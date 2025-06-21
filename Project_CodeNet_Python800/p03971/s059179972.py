n,a,b = map(int,input().split())
s = list(input())
finalists = a + b
rank_b = 0

for i in range(n):
	if s[i] == "a":
		if finalists > 0:
			print("Yes") 
			finalists -= 1
		else:
			print("No")
	elif s[i] == "b":
		rank_b += 1
		if finalists > 0 and rank_b <= b:
			print("Yes") 
			finalists -= 1
		else:
			print("No")
	else:
		print("No")