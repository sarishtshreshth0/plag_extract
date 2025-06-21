def solve():
    A, B = map(int,input().split())
    A_res = func(max(A-1,0))
    B_res = func(B)
    ans = 0
    two_factor = 1
    for i in range(60):
        if not A_res[i] == B_res[i]:
            ans += two_factor
        two_factor *= 2
    
    print(ans)

def func(N):
    res = [0] * 60
    for i in range(60):
        if i == 0 and not (N % 4 == 0 or N % 4 == 3):
            res[i] = 1
        elif N & (1<<i):
            if (N+1) % 2 != 0:
                res[i] = 1

    return res

if __name__ == '__main__':
    solve()