
def resolve():
    N = int(input())
    S = input()
    left, right, cnt = 0,0,0

    for s in S:
        if s == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            right += 1
            cnt = 0

    if cnt>0:
        left = cnt

    ans = "("*right + S + ")"*left
    print(ans)

if __name__ == "__main__":
    resolve()