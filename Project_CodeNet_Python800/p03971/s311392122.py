a = input("").split(" ")
a = [int(b) for b in a]
N = a[0]
A = a[1]
B = a[2]
S = input("")
n = 0
nb = 1
for c in range(len(S)):
    if S[c] == "a":
        if n < (A + B):
            n += 1
            print("Yes")
        else:
            print("No")
    elif S[c] == "b":
        if n < (A + B) and nb <= B:
            n += 1
            nb += 1
            print("Yes")
        else:
            print("No")
    elif S[c] == "c":
        print("No")