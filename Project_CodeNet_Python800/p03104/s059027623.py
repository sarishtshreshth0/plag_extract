A,B = map(int,input().split())
b = list(bin(B))[2:]
b.reverse()
if A%2 == 0:
    if ((B-A)+1)%2 == 0:
        if ((B-A)+1)//2%2 == 0:
            print(0)
        else:
            print(1)
    else:
        if ((B-A)+1)//2%2 == 0:
            print(B)
        else:
            if b[0] == '0':
                print(B+1)
            else:
                print(B-1)
else:
    if ((B-A)+1)%2 == 0:
        if ((B-A)+1)//2%2 == 1:
            print(A^B)
        else:
            print(1^A^B)
    else:
        if ((B-A)+1)//2%2 == 0:
            print(A)
        else:
            print(A^1)