from itertools import product

n = input()

if int(n) < 100:
    print(0)

else:
    ans = 0

    for i in range(3,len(n)+1):
        s = list(product("753",repeat=i))
        for combi in s:
            n_s = "".join(combi)
            if int(n_s) > int(n):
                continue
            if ("7" in combi) and ("5" in combi) and ("3" in combi):
                ans += 1
    
    print(ans)
