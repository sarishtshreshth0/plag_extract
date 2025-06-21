n, a, b = map(int, input().split())
s = str(input())
pass_cnt = 1
kaigai = 0
for i in range(n):
    if(s[i] == "c"):
        # print("No", " それ以外")
        print("No")
    elif(pass_cnt <= (a+b)):
        if(s[i] == "a"):
            # print("Yes", " a pass_cnt= ", pass_cnt)
            print("Yes")
            pass_cnt += 1
        else:
            kaigai += 1
            if(kaigai <= b):
                # print("Yes", " b kaigai= ", kaigai)
                print("Yes")
                pass_cnt += 1
            else:
                print("No")
    else:
        print("No")
