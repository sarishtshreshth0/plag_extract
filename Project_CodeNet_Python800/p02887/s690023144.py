def resolve():
    N = int(input())
    S = input()
    ans = 0
    prev = ""
    for c in S:
        if c == prev:
            continue
        ans += 1
        prev = c
    print(ans)

    
if '__main__' == __name__:
    resolve()