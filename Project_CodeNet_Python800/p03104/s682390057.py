a,b = map(int,input().split())

def bina(x):
    if x % 2 == 1:
        if (x+1) % 4 == 2:
            return 1
        else:
            return 0
    else:
        return x ^ bina(x-1)
    
ans = bina(a-1) ^ bina(b)

print(ans)