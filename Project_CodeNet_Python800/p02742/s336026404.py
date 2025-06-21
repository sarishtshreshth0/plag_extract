def resolve():
    '''
    code here
    '''
    H, W = [int(item) for item in input().split()]

    if H == 1 or W == 1:
        res = 1
    elif H % 2 == 1 and W % 2 == 1:
        res = H * W // 2 +1
    else:
        res = H * W // 2

    print(res)
if __name__ == "__main__":
    resolve()
