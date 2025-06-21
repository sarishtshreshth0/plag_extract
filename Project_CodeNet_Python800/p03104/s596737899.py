a,b=map(int,input().split())

def calc(x):
    n = x // 2 % 2
    if x % 2 :
        if n : return 0
        else: return 1 # 実質(x -1) ^ x の結果
    else:
        return x ^ n 

print(calc(b) ^ calc(a-1))