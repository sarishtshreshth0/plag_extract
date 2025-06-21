import re
A, B = map(int, input().split())
S = input()
print("Yes" if re.fullmatch(r"\d{"+str(A)+r"}-\d{"+str(B)+r"}", S) else "No")