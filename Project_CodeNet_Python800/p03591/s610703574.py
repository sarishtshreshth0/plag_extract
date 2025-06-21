S = input()
SS = list(S)
if len(SS) <= 3:
	print("No")
else:
	if S[0:4] == "YAKI":
		print("Yes")
	else:
		print("No")