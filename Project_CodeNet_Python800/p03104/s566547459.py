A,B = map(int,input().split())

def solve(x):
    if x % 4 == 0:
        return x
    elif x % 4 == 1:
        return 1
    elif x % 4 == 2:
        return x+1
    elif x % 4 == 3:
        return 0
    
print(solve(A-1)^solve(B))