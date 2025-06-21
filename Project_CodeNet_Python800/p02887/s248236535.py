def abc143c_slimes():
    n = int(input())
    s = input()
    cnt = 1
    for i in range(n-1):
        if s[i] != s[i+1]:
            cnt += 1
    print(cnt)
abc143c_slimes()