def resolve():
    s = list(input())
    c = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            if s[i] == "0":
                s[i+1] = "1"
            else:
                s[i+1] = "0"
            c += 1
    print(c)
resolve()