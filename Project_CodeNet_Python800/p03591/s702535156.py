S = input()
if len(S) < 4:
	print("No")
	exit()
else:
	if S[: 4] == "YAKI":
		print("Yes")
	else:
		print("No")
