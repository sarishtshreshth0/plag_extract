n,a,b = list(map(int, input().split()))
s = input()


for c in s:
    if c == 'a' and (a+b) > 0:
        print("Yes")
        a -= 1
    elif c == 'b' and (a + b) > 0 and b > 0:
        print("Yes")
        b -= 1
    else:
        print("No")
