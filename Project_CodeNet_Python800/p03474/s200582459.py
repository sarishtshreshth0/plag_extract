a, b = map(int, input().split())
s = input()

if s[a] != "-":
    print("No")
elif len(s.split("-")) != 2:
    print("No")
else:
    h = s.split("-")
    if len(h[0]) == a and len(h[1]) == b:
        print("Yes")
    else:
        print("No")



