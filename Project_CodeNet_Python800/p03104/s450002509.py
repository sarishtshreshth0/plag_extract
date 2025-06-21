def F(A, B):
    tmp = A
    for i in range(A, B):
        tmp = tmp^(i+1)
    return tmp

def f(A):
    tmp = A%4
    if tmp == 0:
        ans = 0^A
    elif tmp == 1:
        ans = 1
    elif tmp == 2:
        ans = 1^A
    else:
        ans = 0
    return ans

def main():
    A, B = map(int, input().split())
    #print(F(A, B))
    ans = f(B)^f(A-1)
    print(ans)

if __name__ == "__main__":
    main()
