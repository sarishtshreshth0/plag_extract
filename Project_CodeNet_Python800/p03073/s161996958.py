S = input()
length = len(S)

def sim(temp):
    ret = 0
    for i in range(length):
        if S[i] != str(temp):
            ret += 1
        if temp == 0:
            temp = 1
        else:
            temp = 0 
    return ret
    
res1 = sim(0)
res2 = sim(1)
ans = min(res1, res2)
print(ans)