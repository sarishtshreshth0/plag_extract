[A,B] = list(map(int,input().split()))
X = B-A

if A%2 == 0:
    if X%4 ==1:
        out=1
    elif X%4 ==2:
        out=1^B
    elif X%4 ==3:
        out=0
    else:
        out=B

else:
    if X%4 ==1:
        out=A^B
    elif X%4 ==2:
        out=A^1
    elif X%4 ==3:
        out=A^B^1
    else:
        out=A

print(out)
