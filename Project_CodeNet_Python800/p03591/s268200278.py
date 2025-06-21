S = input()
try:
    if S[:4] == "YAKI": print("Yes")
    else: print("No")
except IndexError:
    print("No")