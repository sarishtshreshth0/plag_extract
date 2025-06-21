s = input()
s_len = len(s)
if s_len < 4:
    print("No")
else:
    if s[0:4] == "YAKI":
        print("Yes")
    else:
        print("No")
