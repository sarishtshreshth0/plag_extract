if __name__ == '__main__':
    n = int(input())
    now =""
    list=[]
    flag =True

    for i in range(n):
        s =input()
        if now =="":
            now=s
            list.append(s)
        elif now[len(now)-1] != s[0] or s in list:
            flag=False
            break
        else:
            now=s
            list.append(s)
    if flag:
        print("Yes")
    else:
        print("No")