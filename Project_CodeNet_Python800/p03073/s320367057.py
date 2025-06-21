def solve(i,S):
    t = i
    ret = 0
    for c in S:
        if c != t:
            ret += 1
        t ^= 1
    return ret

S = list(map(int,input()))
print(min(solve(0,S),solve(1,S)))