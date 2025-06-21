def solve(a,b,c):
    return "Yes" if (a < c < b) or (b < c < a) else "No"

a,b,c = map(int, input().split())
print(solve(a,b,c))