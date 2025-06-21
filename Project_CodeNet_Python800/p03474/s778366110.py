a, b = map(int, input().split())
s = input()

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if is_int(s[0:a]) and is_int(s[a+1:a+b+2]) and s[a] == "-":
    print("Yes")
else:
    print("No")
