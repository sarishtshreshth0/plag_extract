M, D = input().split()
cnt = 0

for i in range(22, int(D)+1):
    s = str(i)
    if(int(s[0])*int(s[1]) <= int(M)):
        cnt += 1
        if(int(s[1])<= 1):
            cnt -= 1
print(cnt)