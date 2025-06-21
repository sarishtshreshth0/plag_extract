a, b = list(map(int, input().split()))
s = list(input())
na = "".join(s[: a]).isdigit()
nb = "".join(s[a + 1 :]).isdigit()
hf = s[a]
print("Yes") if na and nb and hf == "-" else print("No")
