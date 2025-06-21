def resolve():
    a, b = map(int, input().split())
    s = input()
    
    flag_len = False
    flag_bar = False
    flag_num = True
    if a+b+1 == len(s):
        flag_len = True
    if s.count("-") == 1 and s[a] == "-":
        flag_bar = True
    if flag_len and flag_bar:
        for i in range(len(s)):
            code = ord(s[i])
            if code < ord("0") or ord("9") < code:
                if code!= ord("-"):
                    flag_num == False
                    break
                
    if flag_len and flag_bar and flag_num:
        print("Yes")
    else:
        print("No")
resolve()