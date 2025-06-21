a, b = map(int, input().split())
s = input()
flag = 1
try :
    num=int(s[0:a])
except :
    flag = 0
if s[a] != "-" :
    flag = 0
try :
    num = int(s[a+1:])
except :
    flag = 0
if flag == 1 :
    print("Yes")
else :
    print("No")
