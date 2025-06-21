def solve():
    X = int(input())
    a,b = divmod(X, 500)
    print(1000*a + 5*(b//5))

if __name__ == "__main__":
    solve()