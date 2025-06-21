def resolve():
    from collections import deque

    def checker(n):
        n = str(n)
        OK3 = False
        OK5 = False
        OK7 = False
        for i in n:
            if i == "3":
                OK3 = True
            elif i== "5":
                OK5 = True
            elif i == "7":
                OK7 = True
        if OK3 and OK5 and OK7:
            return True
        else:
            return False

    n = int(input())
    if n < 357:
        print(0)
    else:
        ans = 0
        nxt = [3, 5, 7]
        nxt = deque(nxt)
        OK = True
        while OK:
            a = nxt.popleft()
            if a > n:
                break
            nxt.append(a*10+3)
            nxt.append(a * 10 + 5)
            nxt.append(a * 10 + 7)
            if checker(a):
                ans += 1
        print(ans)
resolve()