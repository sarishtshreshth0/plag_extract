#!/usr/bin/env python3
# 整数の入力
N = int(input())
ans = 0

def dfs(num, use7, use5, use3):
    if num > N:
        return 0
    else:
        ret = 0
        if use7 == True and use5 == True and use3 == True:
            ret += 1
            #print(num)

        ret += dfs(num*10+7, True, use5, use3)
        ret += dfs(num*10+5, use7, True, use3)
        ret += dfs(num*10+3, use7, use5, True)

    return ret



print(dfs(0, False, False, False))
