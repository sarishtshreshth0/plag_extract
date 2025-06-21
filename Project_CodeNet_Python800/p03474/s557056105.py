#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]


a,b = map(int, input().split())
s = input()

ans = "Yes"
for i in range(len(s)):
    if (i == a):
        if (s[i] != "-"):
            ans = "No"
            break
    else:
        if (s[i] >= "0" and s[i] <= "9"):
            pass
        else:
            ans = "No"
            break
print(ans)



