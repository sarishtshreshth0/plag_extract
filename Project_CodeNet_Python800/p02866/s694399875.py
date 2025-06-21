N = int(input())
D = [int(x) for x in input().split()]

def check():
    if D[0] != 0:
        return False
    t = sorted(list(set(D)))
    if t == list(range(len(t))):
        return True
    return False


def main():
    if check() == False:
        print(0)
        return

    C = {}
    m = 0
    for d in D:
        C[d] = C.get(d,0) + 1
        m = max(m, d)

    if C[0] > 1:
        print(0)
        return

    ans = 1
    for i in range(1,m+1):        
        ans *= (C[i-1] ** C[i])

    print(ans % 998244353)

main()