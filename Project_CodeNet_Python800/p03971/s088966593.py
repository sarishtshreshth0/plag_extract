n,a,b = map(int,input().split())
s = input()
kokunai = 0
kaigai = 0

for i in range(n):
    if s[i] == "a" and a + b > kokunai + kaigai:
        print("Yes")
        kokunai += 1
    elif s[i] == "b" and a + b > kokunai + kaigai and b > kaigai:
        print("Yes")
        kaigai += 1
    else:
        print("No")