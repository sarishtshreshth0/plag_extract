def resolve():
    n = input()
    num = int(n)
    fn = 0
    for i in n:
        fn += int(i)
    ans = ""
    if num % fn == 0:
        ans = "Yes"
    else:
        ans = "No"
    print(ans)
resolve()