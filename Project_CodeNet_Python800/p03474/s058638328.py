a, b = map(int, input().split())
s = input()

def isint(str):
    try: int(str)
    except: return False
    return True

if isint(s[:a]) == True and s[a:a+1] == "-" and isint(s[a+1:]) == True: print("Yes")
else:  print("No")