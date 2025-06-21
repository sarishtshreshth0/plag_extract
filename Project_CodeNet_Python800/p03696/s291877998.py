n=int(input())
s=input()

result=""
cnt=0

#(を追加する
for ss in s:
    #print(result)
    if ss ==")":
        if cnt>0:
            result+=ss
            cnt-=1
        else:
            result="("+result+ss

    else:
        result+=ss
        cnt+=1

L=result.count("(")
R=result.count(")")

result+=")"*(L-R)

print(result)